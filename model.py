from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class carModel(BaseModel):
    code: str = Field(...)
    fullname: str = Field(...)
    category: str = Field(...)
    year: int = Field(..., gt=0, lt=9)

    class Config:
        schema_extra = {
            "example": {
                "code": "John Doe",
                "fullname": "jdoe@x.edu.ng",
                "category": "Water resources engineering",
                "year": 2,
            }
        }