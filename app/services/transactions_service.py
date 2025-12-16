from typing import List

from app.crud.transactions import (
    create_transaction,
    list_transactions,
    list_transactions_since,
    update_transaction,
    delete_transaction,
)

from app.crud.transactions import create_transaction, list_transactions

from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,   # ← 这一行是关键
    TransactionOut,
    TransactionSyncOut,
)
def create_transaction_service(tx: TransactionCreate) -> TransactionOut:
    # 调用 crud 创建数据
    create_transaction(
        household_id=tx.household_id,
        amount_cents=tx.amount_cents,
        note=tx.note
    )
    # 再把刚插入的最新一条取出来（简单写法：按时间倒序取第一条）
    rows = list_transactions()
    latest = rows[0]  # 假设刚插入的一定排在最前
    return TransactionOut(**latest)

def get_transactions_service() -> List[TransactionOut]:
    rows = list_transactions()
    return [TransactionOut(**row) for row in rows]

def update_transaction_service(
    transaction_id: int,
    tx: TransactionUpdate
) -> TransactionOut:
    update_transaction(
        transaction_id=transaction_id,
        amount_cents=tx.amount_cents,
        note=tx.note
    )

    rows = list_transactions()
    for row in rows:
        if row["id"] == transaction_id:
            return TransactionOut(**row)

    raise ValueError("Transaction not found")

def delete_transaction_service(transaction_id: int):
    delete_transaction(transaction_id)

def get_transactions_changes_service(updated_after: str):
    """
    同步用：获取 updated_at 大于指定时间的所有交易（包含软删除）
    """
    rows = list_transactions_since(updated_after)
    return [TransactionSyncOut(**row) for row in rows]
