from fastapi import FastAPI
from typing import List

from app.schemas.transaction import TransactionCreate, TransactionOut
from app.services.transactions_service import (
    create_transaction_service,
    get_transactions_service,
)


app = FastAPI(title="家庭记账 API")



@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/transactions", response_model=TransactionOut)
def add_transaction(tx: TransactionCreate):
    return create_transaction_service(tx)


@app.get("/transactions", response_model=List[TransactionOut])
def get_transactions():
    return get_transactions_service()

