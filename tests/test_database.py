from datetime import datetime
from app.models import ListingDraft, ListingStatus
from app import database


def make_test_draft(draft_id="test-db-001"):
    return ListingDraft(
        id=draft_id,
        title="Database Test Item",
        image_filename="test.jpg",
        created_at=datetime.now(),
        status=ListingStatus.DRAFT
    )


def setup_function():
    # Clear the in-memory store before each test
    database.drafts.clear()


def test_create_and_get_drafts():
    draft = make_test_draft()
    database.create_draft(draft)
    all_drafts = database.get_drafts()
    assert len(all_drafts) == 1
    assert all_drafts[0].id == "test-db-001"


def test_get_draft_by_id_found():
    draft = make_test_draft("find-me-001")
    database.create_draft(draft)
    found = database.get_draft_by_id("find-me-001")
    assert found is not None
    assert found.id == "find-me-001"


def test_get_draft_by_id_not_found():
    result = database.get_draft_by_id("does-not-exist")
    assert result is None


def test_get_drafts_returns_copy():
    draft = make_test_draft("copy-test-001")
    database.create_draft(draft)
    copy = database.get_drafts()
    copy.clear()
    assert len(database.get_drafts()) == 1