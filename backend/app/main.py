from fastapi import FastAPI

app = FastAPI(title="AI Financial Analytics API")

@app.get("/")
def root():
    return {"status": "Backend running"}