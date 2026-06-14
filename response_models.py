from pydantic import BaseModel
from typing import List

class URLCheckResponse(BaseModel):
    url: str
    is_phishing: bool
    risk_score: int  # Scale from 0 to 100
    flags: List[str]
    details: dict