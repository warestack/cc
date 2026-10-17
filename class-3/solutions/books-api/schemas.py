from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    year: int = Field(ge=1900)


class BookResponse(BookCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
