from typing import Dict, Any

def lookup_market_data(classification: Dict[str, Any]) -> Dict[str, Any]:
    brand = classification.get("brand", "")
    item_name = classification.get("item_name", "")
    category = classification.get("category", "")

    parts = [p for p in [brand, item_name, category] if p]
    query_used = " ".join(parts).strip()
    

    return {
        "query_used": query_used,
        "active_comps": [],
        "sold_comps": [],
        "fallback_comps": [],
        "price_low": None,
        "price_mid": None,
        "price_high": None,
        "median_price": None,
        "outlier_count": 0,
        "confidence": 0.0,
        "source_used": "stub",
        "source": "stub",
        "match_strategy": "exact"
    }