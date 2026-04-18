from fastapi import FastAPI, File, UploadFile
from config import APP_ENV
from uuid import uuid4
from datetime import datetime
from app.models import ListingDraft, ListingStatus
from app.database import create_draft, get_drafts

app = FastAPI(title="eBay Lister AI App")

@app.get("/")
def read_root():
    return {
        "message": "eBay Lister AI backend is running",
        "environment": APP_ENV
    }

@app.post("/upload-photo")
async def upload_photo(file: UploadFile = File(...)):
    draft_id = str(uuid4())
    draft = ListingDraft(
        id=draft_id,
        title="Placeholder title",
        image_filename=file.filename,
        created_at=datetime.now(),
        status=ListingStatus.DRAFT,
        notes=[]
    )
    create_draft(draft)
    return{
        "draft_id": draft_id,
        "filename": file.filename,
        "status": draft.status.value
    }

@app.get("/drafts")
def list_drafts():
    return {"drafts": [d.__dict__ for d in get_drafts()]}