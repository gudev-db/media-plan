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
        "nome": nome.strip(),
        "empresa": None,
        "cargo": None,
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
