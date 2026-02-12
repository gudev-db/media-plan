from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from bson import ObjectId

def save_plan(
    db, user_id: ObjectId, nome_plano: str, params: Dict, resultado: Dict
) -> ObjectId:
    plan = {
        "user_id": user_id,
        "nome_plano": nome_plano,
        "params": params,
        "resultado": resultado,
        "criado_em": datetime.now(timezone.utc),
        "atualizado_em": datetime.now(timezone.utc),
    }
    result = db.plans.insert_one(plan)
    return result.inserted_id

def get_user_plans(
    db, user_id: ObjectId, limit: int = 20, skip: int = 0
) -> List[Dict]:
    cursor = (
        db.plans.find({"user_id": user_id})
        .sort("criado_em", -1)
        .skip(skip)
        .limit(limit)
    )
    return list(cursor)

def get_plan_by_id(
    db, plan_id: ObjectId, user_id: ObjectId
) -> Optional[Dict]:
    return db.plans.find_one({"_id": plan_id, "user_id": user_id})

def delete_plan(db, plan_id: ObjectId, user_id: ObjectId) -> bool:
    result = db.plans.delete_one({"_id": plan_id, "user_id": user_id})
    return result.deleted_count > 0

def count_user_plans(db, user_id: ObjectId) -> int:
    return db.plans.count_documents({"user_id": user_id})
