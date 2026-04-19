from fastapi import FastAPI, File, UploadFile
from config import APP_ENV
from uuid import uuid4
from datetime import datetime
from app.models import ListingDraft, ListingStatus
from app.database import create_draft, get_drafts
from app.ai.recognition import classify_item

app = FastAPI(title="eBay Lister AI App")


@app.get("/")
def read_root():
    return {
        "message": "eBay Lister AI backend is running",
        "environment": APP_ENV
    }


@app.post("/upload-photo")
async def upload_photo(file: UploadFile = File(...)):
    if file.filename is None:
        raise ValueError("Uploaded file must have a filename")

    draft_id = str(uuid4())
    classification_result = classify_item(file.filename)

    draft = ListingDraft(
        id=draft_id,
        title="Placeholder title",
        image_filename=file.filename,
        created_at=datetime.now(),
        status=ListingStatus.DRAFT,
        notes=[],
        debug_notes=[
            "Draft created from uploaded photo",
            "Classification stub executed successfully"
        ],
        classification=classification_result
    )

    create_draft(draft)

    return {
        "draft_id": draft_id,
        "filename": file.filename,
        "status": draft.status.value,
        "classification": classification_result
    }


@app.get("/drafts")
def list_drafts():
    return {
        "drafts": [
            {
                "id": d.id,
                "title": d.title,
                "image_filename": d.image_filename,
                "created_at": d.created_at.isoformat(),
                "status": d.status.value,
                "notes": d.notes,
                "debug_notes": d.debug_notes,
                "classification": d.classification
            }
            for d in get_drafts()
        ]
    }