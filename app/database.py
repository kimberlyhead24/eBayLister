from typing import List, Optional
from app.models import ListingDraft

drafts: List[ListingDraft] = []

def create_draft(draft: ListingDraft) -> None:
    drafts.append(draft)

def get_drafts() -> List[ListingDraft]:
    return drafts[:]

def get_draft_by_id(draft_id: str) -> Optional[ListingDraft]:
    for draft in drafts:
        if draft.id == draft_id:
            return draft
    return None