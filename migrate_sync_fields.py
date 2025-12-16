import sqlite3
from pathlib import Path

DB_PATH = Path("family.db")

def column_exists(conn, table: str, column: str) -> bool:
    cur = conn.execute(f"PRAGMA table_info({table})")
    cols = [row[1] for row in cur.fetchall()]
    return column in cols

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. 添加 updated_at（默认使用 NULL）
    if not column_exists(conn, "transactions", "updated_at"):
        print("Adding column updated_at to transactions...")
        cur.execute(
            "ALTER TABLE transactions ADD COLUMN updated_at TEXT"
        )
        # 给已有数据补上当前时间
        cur.execute(
            "UPDATE transactions SET updated_at = datetime('now')"
        )

    # 2. 添加 is_deleted（默认 0）
    if not column_exists(conn, "transactions", "is_deleted"):
        print("Adding column is_deleted to transactions...")
        cur.execute(
            "ALTER TABLE transactions ADD COLUMN is_deleted INTEGER DEFAULT 0"
        )
        # 补齐已有数据的默认值
        cur.execute(
            "UPDATE transactions SET is_deleted = 0 WHERE is_deleted IS NULL"
        )

    conn.commit()
    conn.close()
    print("Migration done.")

if __name__ == "__main__":
    migrate()
