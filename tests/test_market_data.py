from app.services.market_data import lookup_market_data


def test_lookup_market_data_returns_expected_keys():
    classification = {
        "item_name": "coffee grinder",
        "brand": "Cuisinart",
        "category": "Kitchen Tools",
        "condition_hint": "used",
        "confidence": 0.75
    }
    result = lookup_market_data(classification)
    assert "query_used" in result
    assert "active_comps" in result
    assert "sold_comps" in result
    assert "price_low" in result
    assert "price_mid" in result
    assert "price_high" in result
    assert "outlier_count" in result
    assert "confidence" in result
    assert "source" in result


def test_lookup_market_data_query_uses_classification():
    classification = {
        "item_name": "coffee grinder",
        "brand": "Cuisinart",
        "category": "Kitchen Tools",
        "condition_hint": "used",
        "confidence": 0.75
    }
    result = lookup_market_data(classification)
    assert "Cuisinart" in result["query_used"]
    assert "coffee grinder" in result["query_used"]


def test_lookup_market_data_empty_classification():
    result = lookup_market_data({})
    assert "query_used" in result
    assert result["query_used"] == ""


def test_lookup_market_data_comps_are_lists():
    classification = {
        "item_name": "lamp",
        "brand": "unknown brand",
        "category": "Home Decor",
        "condition_hint": "good",
        "confidence": 0.5
    }
    result = lookup_market_data(classification)
    assert isinstance(result["active_comps"], list)
    assert isinstance(result["sold_comps"], list)


def test_lookup_market_data_source_is_stub():
    result = lookup_market_data({
        "item_name": "test",
        "brand": "test",
        "category": "test",
        "condition_hint": "used",
        "confidence": 0.0
    })
    assert result["source"] == "stub"
    assert result["source_used"] == "stub"