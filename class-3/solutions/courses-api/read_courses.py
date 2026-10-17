import models
from database import SessionLocal

db = SessionLocal()

try:
    # Query the Course model. SQLAlchemy translates this into SELECT * FROM courses.
    courses = db.query(models.Course).all()

    for course in courses:
        print(course.id, course.code, course.title, course.lecturer)

finally:
    db.close()
