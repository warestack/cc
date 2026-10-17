import models
from database import SessionLocal, engine

# Create all tables described by the models.
# If the courses table does not exist yet, this line creates it.
models.Base.metadata.create_all(bind=engine)

# Open a database session.
# We use this session to add, query, commit, and close database work.
db = SessionLocal()

try:
    courses = [
        models.Course(code="CC101", title="Cloud Computing", lecturer="Stelios"),
        models.Course(code="DB101", title="Databases", lecturer="Maria"),
    ]

    for course in courses:
        # Check by course code first so running seed.py twice does not add duplicates.
        existing_course = (
            db.query(models.Course)
            .filter(models.Course.code == course.code)
            .first()
        )

        if existing_course is None:
            db.add(course)

    # commit() saves the pending inserts to courses.db.
    db.commit()

    print("Database created and courses checked.")

finally:
    # Always close the session when the database work is finished.
    db.close()
