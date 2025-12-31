from fastapi import FastAPI
from app.core.config import settings
from app.routers.analytics import router as analytics_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(analytics_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}