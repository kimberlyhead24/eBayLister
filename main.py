from fastapi import FastAPI
from config import APP_ENV

app = FastAPI(title="eBay Lister AI App")

@app.get("/")
def read_root():
    return {
        "message": "eBay Lister AI backend is running",
        "environment": APP_ENV
    }