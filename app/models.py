from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any, Optional

class ListingStatus(Enum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
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
    notes: List[str] = field(default_factory=list)
    debug_notes: List[str] = field(default_factory=list)
    classification: Dict[str, Any] = field(default_factory=dict)
    market_data: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    seller_notes: str = ""
    business_review_status: str = "pending"
    business_review_notes: str = ""
    created_by: str = "seller"
    reviewed_by: Optional[str] = None
    approved_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None
