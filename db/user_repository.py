from datetime import datetime, timezone
from typing import Optional, Dict, Any
import bcrypt
from bson import ObjectId

def create_user_email(db, email: str, password: str, nome: str) -> Dict[str, Any]:
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")
    now = datetime.now(timezone.utc)
    user = {
        "email": email.lower().strip(),
        "password_hash": password_hash,
        "auth_provider": "email",
        "google_sub": None,
        "nome": nome.strip(),
        "empresa": None,
        "cargo": None,
        "avatar_url": None,
        "criado_em": now,
        "atualizado_em": now,
        "ultimo_login": now,
    }
    result = db.users.insert_one(user)
    user["_id"] = result.inserted_id
    return user

def verify_password(db, email: str, password: str) -> Optional[Dict[str, Any]]:
    user = db.users.find_one({"email": email.lower().strip()})
    if user and user.get("password_hash"):
        if bcrypt.checkpw(
            password.encode("utf-8"), user["password_hash"].encode("utf-8")
        ):
            db.users.update_one(
                {"_id": user["_id"]},
                {"$set": {"ultimo_login": datetime.now(timezone.utc)}},
            )
            return user
    return None

def find_or_create_google_user(
    db, google_sub: str, email: str, nome: str, avatar_url: str = None
) -> Dict[str, Any]:
    existing = db.users.find_one(
        {"$or": [{"google_sub": google_sub}, {"email": email.lower()}]}
    )
    now = datetime.now(timezone.utc)

    if existing:
        update_fields = {
            "google_sub": google_sub,
            "ultimo_login": now,
            "atualizado_em": now,
        }
        if existing["auth_provider"] == "email":
            update_fields["auth_provider"] = "both"
        if avatar_url:
            update_fields["avatar_url"] = avatar_url
        if nome and not existing.get("nome"):
            update_fields["nome"] = nome

        db.users.update_one({"_id": existing["_id"]}, {"$set": update_fields})
        existing.update(update_fields)
        return existing

    user = {
        "email": email.lower().strip(),
        "password_hash": None,
        "auth_provider": "google",
        "google_sub": google_sub,
        "nome": nome or email.split("@")[0],
        "empresa": None,
        "cargo": None,
        "avatar_url": avatar_url,
        "criado_em": now,
        "atualizado_em": now,
        "ultimo_login": now,
    }
    result = db.users.insert_one(user)
    user["_id"] = result.inserted_id
    return user

def update_profile(db, user_id: ObjectId, updates: Dict[str, Any]) -> bool:
    """Atualiza campos do perfil. Apenas campos permitidos."""
    allowed = {"nome", "empresa", "cargo"}
    safe_updates = {k: v for k, v in updates.items() if k in allowed and v is not None}
    if not safe_updates:
        return False
    safe_updates["atualizado_em"] = datetime.now(timezone.utc)
    result = db.users.update_one({"_id": user_id}, {"$set": safe_updates})
    return result.modified_count > 0

def get_user_by_id(db, user_id: ObjectId) -> Optional[Dict[str, Any]]:
    """Busca usuário por ObjectId."""
    return db.users.find_one({"_id": user_id})
