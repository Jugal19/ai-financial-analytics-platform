from app.routers.analytics import router
from app.db.mongo import get_db
from fastapi import Depends

@router.get("/summary")
def analytics_summary(db=Depends(get_db)):
    transactions = list(db.transactions.find())

    total_income = sum(
        t["amount"] for t in transactions if t["type"] == "income"
    )

    total_expenses = sum(
        t["amount"] for t in transactions if t["type"] == "expense"
    )

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_savings": total_income - total_expenses
    }