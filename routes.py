from fastapi import APIRouter, HTTPException
from app.models.request_models import URLCheckRequest
from app.models.response_models import URLCheckResponse
from app.services.reputation_service import ReputationService

router = APIRouter()

@router.post("/analyze", response_model=URLCheckResponse)
def analyze_url(payload: URLCheckRequest):
    if not payload.url:
        raise HTTPException(status_code=400, detail="URL cannot be empty")
        
    result = ReputationService.evaluate_url(payload.url)
    return result