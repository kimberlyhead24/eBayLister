from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any

class ListingStatus(Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    PUBLISHED = "published"
    FAILED = "failed"

@dataclass
class ListingDraft:
    id: str
    title: str
    image_filename: str
    created_at: datetime
    status: ListingStatus
    notes: List[str]
    debug_notes: List[str] 
    classification: Dict[str, Any]
    