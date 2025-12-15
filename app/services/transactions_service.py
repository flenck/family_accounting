from typing import List

from app.crud.transactions import create_transaction, list_transactions
from app.schemas.transaction import TransactionCreate, TransactionOut

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
