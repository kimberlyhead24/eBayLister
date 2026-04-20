from typing import Dict, Any

def classify_item(file_bytes: bytes, filename: str) -> Dict[str, Any]:
    size_bytes = len(file_bytes)
   
    return {
        "item_name": "unknown item",
        "brand": "unknown brand",
        "category": "unknown category",
        "condition_hint": "unknown condition",
        "confidence": 0.0,
        "filename": filename,
        "byte_count": size_bytes,
        "classifier_version": "stub-v1"
    }