from pydantic import BaseModel
from typing import Optional


class TransactionCreate(BaseModel):
    household_id: int
    amount_cents: int
    note: Optional[str] = None


class TransactionUpdate(BaseModel):
    amount_cents: int
    note: Optional[str] = None


class TransactionOut(BaseModel):
    id: int
    household_id: int
    amount_cents: int
    note: Optional[str]
    occurred_at: str


class TransactionSyncOut(BaseModel):
    id: int
    household_id: int
    amount_cents: int
    note: Optional[str]
    updated_at: str
    is_deleted: bool
