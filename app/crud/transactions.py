from app.db import get_connection
from typing import Optional
from typing import List, Dict

def create_transaction(
    household_id: int,
    amount_cents: int,
    note: Optional[str]
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (
            household_id,
            amount_cents,
            note,
            occurred_at,
            updated_at,
            is_deleted
        )
        VALUES (?, ?, ?, datetime('now'), datetime('now'), 0)
    """, (household_id, amount_cents, note))

    conn.commit()
    conn.close()

def list_transactions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, household_id, amount_cents, note, occurred_at
        FROM transactions
        ORDER BY occurred_at DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]




    conn.commit()
    conn.close()


def list_transactions_since(updated_after: str) -> List[Dict]:
    """
    同步用：返回 updated_at 大于指定时间的所有交易（包含软删除记录）。
    updated_after 格式示例：'2025-01-01 00:00:00'
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               household_id,
               amount_cents,
               note,
               occurred_at,
               updated_at,
               is_deleted
        FROM transactions
        WHERE updated_at > ?
        ORDER BY updated_at ASC
    """, (updated_after,))

    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def update_transaction(
    transaction_id: int,
    amount_cents: int,
    note: Optional[str]
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET amount_cents = ?,
            note = ?,
            updated_at = datetime('now')
        WHERE id = ? AND is_deleted = 0
    """, (amount_cents, note, transaction_id))

    conn.commit()
    conn.close()

def delete_transaction(transaction_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET is_deleted = 1,
            updated_at = datetime('now')
        WHERE id = ? AND is_deleted = 0
    """, (transaction_id,))

    conn.commit()
    conn.close()
