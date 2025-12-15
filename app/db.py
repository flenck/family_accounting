import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "family.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # 让查询结果像 dict
    return conn
