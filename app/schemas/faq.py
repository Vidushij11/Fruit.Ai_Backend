from pydantic import BaseModel

class FAQBase(BaseModel):
    question: str
    answer: str

class FAQCreate(FAQBase):
    pass

class FAQUpdate(FAQBase):
    pass

class FAQ(FAQBase):
    id: int

    class Config:
        orm_mode = True