from app.ai.recognition import classify_item


def test_classify_item_returns_expected_keys():
    fake_bytes = b"fake image bytes"
    result = classify_item(fake_bytes, "test_item.jpg")
    assert "item_name" in result
    assert "brand" in result
    assert "category" in result
    assert "condition_hint" in result
    assert "confidence" in result
    assert "filename" in result
    assert "byte_count" in result


def test_classify_item_byte_count():
    fake_bytes = b"hello world"
    result = classify_item(fake_bytes, "test.jpg")
    assert result["byte_count"] == len(fake_bytes)


def test_classify_item_filename_stored():
    fake_bytes = b"data"
    result = classify_item(fake_bytes, "my_product.jpg")
    assert result["filename"] == "my_product.jpg"


def test_classify_item_confidence_is_float():
    result = classify_item(b"data", "item.jpg")
    assert isinstance(result["confidence"], float)