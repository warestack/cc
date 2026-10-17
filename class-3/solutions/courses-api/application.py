from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import schemas
import models
from database import engine, get_db

def create_app(db_engine=engine):
    models.Base.metadata.create_all(bind=db_engine)
    app = FastAPI()

    @app.get("/")
    def home():
        return {"message": "Week 3 SQLAlchemy API is running"}


    @app.get("/courses", response_model=list[schemas.CourseResponse])
    def get_courses(db: Session = Depends(get_db)):
        # response_model tells FastAPI to return a list of CourseResponse objects.
        # Read all courses from the database.
        courses = db.query(models.Course).all()
        return courses


    @app.get("/courses/{course_id}", response_model=schemas.CourseResponse)
    def get_course(course_id: int, db: Session = Depends(get_db)):
        # Find one course by primary key.
        course = db.query(models.Course).filter(models.Course.id == course_id).first()

        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")

        return course


    @app.post("/courses", response_model=schemas.CourseResponse, status_code=201)
    def create_course(course_data: schemas.CourseCreate, db: Session = Depends(get_db)):
        # course_data has already been checked by Pydantic.
        # We can use dot notation because course_data is a CourseCreate object.
        course = models.Course(
            code=course_data.code,
            title=course_data.title,
            lecturer=course_data.lecturer
        )

        try:
            db.add(course)
            db.commit()
            db.refresh(course)
            return course

        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Course code already exists")

    return app
