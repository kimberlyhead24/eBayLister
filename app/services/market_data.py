from typing import Dict, Any

def lookup_market_data(classification: Dict[str, Any]) -> Dict[str, Any]:
    query_used = " ".join(
        [
            classification.get("brand", ""),
            classification.get("item_name", ""),
            classification.get("category", "")
        ]
    ).strip()

    return {
        "source_used": "ebay" or "google_shopping" or "none",
        "match_strategy": "exact" or "similar" or "none",
        "query_used": "...",
        "active_comps": [],
        "sold_comps": [],
        "fallback_comps": [],
        "price_low": None,
        "price_mid": None,
        "price_high": None,
        "median_price": None,
        "outlier_count": 0,
        "confidence": 0.0
    }