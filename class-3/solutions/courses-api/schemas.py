from pydantic import BaseModel, ConfigDict, Field


# Data accepted when creating a course.
# This schema describes the request body for POST /courses.
class CourseCreate(BaseModel):
    # Field adds validation rules before the route function runs.
    code: str = Field(min_length=2, max_length=20)
    title: str = Field(min_length=3, max_length=100)
    lecturer: str = Field(min_length=2, max_length=80)


# Data returned by the API.
# This schema describes the response shape sent back to the client.
class CourseResponse(BaseModel):
    id: int
    code: str
    title: str
    lecturer: str

    # This allows Pydantic to read values from SQLAlchemy objects.
    model_config = ConfigDict(from_attributes=True)
