from fastapi import APIRouter
from app.api.api_v1.endpoints import faqs

api_router = APIRouter()
api_router.include_router(faqs.router, prefix="/faqs", tags=["faqs"])