from fastapi import FastAPI, File, UploadFile, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from typing import List, Optional
from config import APP_ENV
from uuid import uuid4
from datetime import datetime
from app.models import ListingDraft, ListingStatus
from app.database import create_draft, get_drafts, get_draft_by_id
from app.ai.recognition import classify_item
from app.services.market_data import lookup_market_data

app = FastAPI(title="eBay Lister AI App")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ── API health check ──────────────────────────────────────────
@app.get("/")
def read_root():
    return {
        "message": "eBay Lister AI backend is running",
        "environment": APP_ENV
    }


# ── Upload screen ─────────────────────────────────────────────
@app.get("/ui")
def upload_screen(request: Request):
    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )


# ── Review screen ─────────────────────────────────────────────
@app.get("/review/{draft_id}")
def review_screen(request: Request, draft_id: str):
    draft = get_draft_by_id(draft_id)

    if not draft:
        return templates.TemplateResponse(
            "upload.html",
            {
                "request": request,
                "error": f"Draft {draft_id} not found."
            }
        )

    draft_dict = {
        "id": draft.id,
        "title": draft.title,
        "image_filename": draft.image_filename,
        "created_at": draft.created_at.isoformat(),
        "status": draft.status.value,
        "notes": draft.notes,
        "debug_notes": draft.debug_notes,
        "classification": draft.classification,
        "market_data": draft.market_data,
        "metadata": draft.metadata,
        "seller_notes": draft.seller_notes,
        "business_review_status": draft.business_review_status,
        "business_review_notes": draft.business_review_notes,
        "created_by": draft.created_by,
        "reviewed_by": draft.reviewed_by,
        "approved_by": draft.approved_by,
        "reviewed_at": draft.reviewed_at.isoformat() if draft.reviewed_at else None,
        "approved_at": draft.approved_at.isoformat() if draft.approved_at else None
    }

    return templates.TemplateResponse(
        "review.html",
        {"request": request, "draft": draft_dict}
    )


# ── Multi-photo upload API ────────────────────────────────────
@app.post("/upload-photos")
async def upload_photos(
    files: List[UploadFile] = File(...),
    seller_notes: Optional[str] = Form(""),
    item_hint: Optional[str] = Form(""),
    condition_hint: Optional[str] = Form(""),
    msrp: Optional[str] = Form(""),
    listing_type: Optional[str] = Form("fixed"),
    quantity: Optional[str] = Form("1"),
    shipping_carrier: Optional[str] = Form("usps"),
    allow_offers: Optional[str] = Form("yes"),
):
    if not files or len(files) == 0:
        return JSONResponse(
            status_code=400,
            content={"detail": "At least one photo is required."}
        )

    primary_file = files[0]
    primary_bytes = await primary_file.read()

    classification_result = classify_item(primary_bytes, primary_file.filename or "unknown")
    market_data_result = lookup_market_data(classification_result)

    draft_id = str(uuid4())

    all_filenames = []
    for f in files:
        if f.filename:
            all_filenames.append(f.filename)

    draft = ListingDraft(
        id=draft_id,
        title=item_hint if item_hint else "Placeholder title",
        image_filename=primary_file.filename or "unknown",
        created_at=datetime.now(),
        status=ListingStatus.DRAFT,
        debug_notes=[
            f"Draft created with {len(files)} photo(s)",
            "Classification stub executed",
            "Market data stub executed"
        ],
        classification=classification_result,
        market_data=market_data_result,
                metadata={
            "upload_content_type": primary_file.content_type,
            "upload_size_bytes": len(primary_bytes),
            "all_filenames": all_filenames,
            "photo_count": len(files),
            "listing_type": listing_type,
            "quantity": quantity,
            "shipping_carrier": shipping_carrier,
            "allow_offers": allow_offers,
            "msrp": msrp
        },
        seller_notes=seller_notes or "",
        business_review_status="pending",
        business_review_notes="",
        created_by="seller"
    )

    create_draft(draft)

    return {
        "draft_id": draft_id,
        "filename": primary_file.filename,
        "photo_count": len(files),
        "status": draft.status.value,
        "classification": classification_result,
        "market_data": market_data_result
    }


# ── All drafts API ────────────────────────────────────────────
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
                "photo_count": d.metadata.get("photo_count", 1),
                "classification": d.classification,
                "market_data": d.market_data,
                "seller_notes": d.seller_notes,
                "business_review_status": d.business_review_status,
                "created_by": d.created_by
            }
            for d in get_drafts()
        ]
    }