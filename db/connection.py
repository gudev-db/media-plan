import os
from pymongo import MongoClient
import streamlit as st

@st.cache_resource
def get_database():
    uri = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    db_name = os.getenv("MONGO_DB_NAME", "media_plan")
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    db = client[db_name]
    _ensure_indexes(db)
    return db

def _ensure_indexes(db):
    db.users.create_index("email", unique=True)
    db.users.create_index("google_sub", unique=True, sparse=True)
    db.plans.create_index("user_id")
    db.plans.create_index([("user_id", 1), ("criado_em", -1)])
