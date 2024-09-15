from fastapi import APIRouter, HTTPException
from app.schemas.faq import FAQ, FAQCreate, FAQUpdate

router = APIRouter()

# In-memory list to store FAQs
faqs = []

@router.get("/", response_model=list[FAQ])
async def read_faqs(skip: int = 0, limit: int = 10):
    return faqs[skip:skip + limit]

@router.get("/{faq_id}", response_model=FAQ)
async def read_faq(faq_id: int):
    for faq in faqs:
        if faq.id == faq_id:
            return faq
    raise HTTPException(status_code=404, detail="FAQ not found")

@router.post("/", response_model=FAQ)
async def create_faq(faq: FAQCreate):
    new_faq = FAQ(id=len(faqs) + 1, **faq.dict())
    faqs.append(new_faq)
    return new_faq

@router.put("/{faq_id}", response_model=FAQ)
async def update_faq(faq_id: int, faq: FAQUpdate):
    for index, existing_faq in enumerate(faqs):
        if existing_faq.id == faq_id:
            updated_faq = existing_faq.copy(update=faq.dict())
            faqs[index] = updated_faq
            return updated_faq
    raise HTTPException(status_code=404, detail="FAQ not found")

@router.delete("/{faq_id}", response_model=FAQ)
async def delete_faq(faq_id: int):
    for index, faq in enumerate(faqs):
        if faq.id == faq_id:
            return faqs.pop(index)
    raise HTTPException(status_code=404, detail="FAQ not found")