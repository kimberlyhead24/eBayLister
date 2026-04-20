import pytest
from fastapi.testclient import TestClient
from app import database
from main import app

client = TestClient(app)


def setup_function():
    database.drafts.clear()


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_upload_screen_loads():
    response = client.get("/ui")
    assert response.status_code == 200
    assert b"Create New Listing" in response.content


def test_upload_photos_no_files():
    response = client.post("/upload-photos")
    assert response.status_code in [400, 422]


def test_upload_photos_with_file():
    fake_image = b"\xff\xd8\xff" + b"\x00" * 100
    response = client.post(
        "/upload-photos",
        files=[("files", ("test.jpg", fake_image, "image/jpeg"))],
        data={"seller_notes": "Test notes", "item_hint": "Test item"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "draft_id" in data
    assert "status" in data
    assert data["status"] == "draft"
    assert data["photo_count"] == 1


def test_upload_multiple_photos():
    fake_image = b"\xff\xd8\xff" + b"\x00" * 100
    response = client.post(
        "/upload-photos",
        files=[
            ("files", ("photo1.jpg", fake_image, "image/jpeg")),
            ("files", ("photo2.jpg", fake_image, "image/jpeg")),
            ("files", ("photo3.jpg", fake_image, "image/jpeg"))
        ],
        data={"seller_notes": "Multiple photo test"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["photo_count"] == 3


def test_review_screen_loads_after_upload():
    fake_image = b"\xff\xd8\xff" + b"\x00" * 100
    upload_response = client.post(
        "/upload-photos",
        files=[("files", ("test.jpg", fake_image, "image/jpeg"))],
        data={"item_hint": "Vintage lamp"}
    )
    assert upload_response.status_code == 200
    draft_id = upload_response.json()["draft_id"]

    review_response = client.get(f"/review/{draft_id}")
    assert review_response.status_code == 200
    assert b"Draft Review" in review_response.content


def test_review_screen_unknown_draft():
    response = client.get("/review/nonexistent-id-999")
    assert response.status_code == 200
    assert b"New Listing" in response.content


def test_drafts_api_returns_list():
    response = client.get("/drafts")
    assert response.status_code == 200
    assert "drafts" in response.json()


def test_drafts_api_after_upload():
    fake_image = b"\xff\xd8\xff" + b"\x00" * 100
    client.post(
        "/upload-photos",
        files=[("files", ("item.jpg", fake_image, "image/jpeg"))],
        data={"item_hint": "Camera"}
    )
    response = client.get("/drafts")
    assert response.status_code == 200
    drafts = response.json()["drafts"]
    assert len(drafts) == 1
    assert drafts[0]["status"] == "draft"