from app.db import get_connection

def create_transaction(household_id: int, amount_cents: int, note: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (household_id, amount_cents, note, occurred_at)
        VALUES (?, ?, ?, datetime('now'))
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
