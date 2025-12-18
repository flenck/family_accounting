from fastapi import FastAPI
from typing import List

from app.schemas.transaction import (
    TransactionCreate,
    TransactionOut,
    TransactionSyncOut,
    TransactionUpdate,
)

from app.services.transactions_service import (
    create_transaction_service,
    get_transactions_service,
    get_transactions_changes_service,
    update_transaction_service,
    delete_transaction_service,
)



from app.schemas.transaction import TransactionCreate, TransactionOut
from app.services.transactions_service import (
    create_transaction_service,
    get_transactions_service,
)


app = FastAPI(title="家庭记账 API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发阶段先全放开
    allow_credentials=True,
    allow_methods=["*"],  # 关键：允许 OPTIONS
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/transactions", response_model=TransactionOut)
def add_transaction(tx: TransactionCreate):
    return create_transaction_service(tx)


@app.get("/transactions", response_model=List[TransactionOut])
def get_transactions():
    return get_transactions_service()


@app.put("/transactions/{transaction_id}", response_model=TransactionOut)
def update_transaction_api(
    transaction_id: int,
    tx: TransactionUpdate
):
    return update_transaction_service(transaction_id, tx)

@app.delete("/transactions/{transaction_id}")
def delete_transaction_api(transaction_id: int):
    delete_transaction_service(transaction_id)
    return {"status": "deleted"}

from fastapi import Query
from app.schemas.transaction import TransactionSyncOut
from app.services.transactions_service import get_transactions_changes_service
from typing import List

@app.get(
    "/transactions/changes",
    response_model=List[TransactionSyncOut],
    summary="Get incremental transaction changes"
)
def get_transaction_changes(
    updated_after: str = Query(
        ...,
        description="Return transactions updated after this timestamp (YYYY-MM-DD HH:MM:SS)"
    )
):
    return get_transactions_changes_service(updated_after)
