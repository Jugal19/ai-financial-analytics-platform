from app.routers.analytics import router
from app.db.mongo import get_db
from fastapi import Depends
from collections import defaultdict

@router.get("/trends")
def analytics_trends(db=Depends(get_db)):
    transactions = list(db.transactions.find())

    monthly = defaultdict(float)

    for t in transactions:
        if t["type"] == "expense":
            month = t["date"].strftime("%Y-%m")
            monthly[month] += t["amount"]

    return dict(sorted(monthly.items()))