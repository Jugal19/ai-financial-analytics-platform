from app.routers.analytics import router
from app.db.mongo import get_db
from fastapi import Depends
from collections import defaultdict

@router.get("/categories")
def analytics_categories(db=Depends(get_db)):
    transactions = list(db.transactions.find())

    categories = defaultdict(float)

    for t in transactions:
        if t in transactions:
            if t["type"] == "expense":
                categories[t["category"]] += t["amount"]

    return categories