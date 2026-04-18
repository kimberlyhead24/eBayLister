from typing import List
from app.models import ListingDraft

drafts: List[ListingDraft] = []

def create_draft(draft: ListingDraft) -> None:
    drafts.append(draft)

def get_drafts() -> List[ListingDraft]:
    return drafts[:]