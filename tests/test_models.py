from datetime import datetime
from app.models import ListingDraft, ListingStatus

def test_listing_draft_creation():
    draft = ListingDraft(
        id="test-001",
        title="Test Item",
        image_filename="test.jpg",
        created_at=datetime.now(),
        status=ListingStatus.DRAFT
    )

    assert draft.id == "test-001"
    assert draft.title == "Test Item"
    assert draft.status == ListingStatus.DRAFT
    assert draft.notes == []
    assert draft.debug_notes == []
    assert draft.classification == {}
    assert draft.market_data == {}
    assert draft.seller_notes == ""
    assert draft.business_review_status == "pending"
    assert draft.created_by == "seller"
    assert draft.reviewed_by is None
    assert draft.approved_by is None

def test_listing_status_values():
    assert ListingStatus.DRAFT.value == "draft"
    assert ListingStatus.APPROVED.value == "approved"
    assert ListingStatus.PUBLISHED.value == "published"
    assert ListingStatus.FAILED.value == "failed"