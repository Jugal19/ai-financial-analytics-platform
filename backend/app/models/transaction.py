from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal

class Transaction(BaseModel):
    date: datetime
    category: str
    amount: float
    type: Literal['income', 'expense']