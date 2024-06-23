from sqlalchemy import create_engine, ForeignKey, Column, Integer, NVARCHAR, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, joinedload

BASE = declarative_base()

class STUDENT(BASE):
    __tablename__ = "Student"
    ID = Column(Integer, primary_key=True)
    NAME = Column(NVARCHAR(20))
    SURNAME = Column(NVARCHAR(20))
    notes = relationship("NOTES", back_populates="student")

    def __init__(self, NAME: str, SURNAME: str):
        self.NAME = NAME
        self.SURNAME = SURNAME

    def __repr__(self):
        return f"{self.NAME} {self.SURNAME}"

class CITY(BASE):
    __tablename__ = "City"
    ID = Column(Integer, primary_key=True)
    NAME = Column(NVARCHAR(20))
    REGION = Column(NVARCHAR(20))

    def __init__(self, NAME: str, REGION: str):
        self.NAME = NAME
        self.REGION = REGION

    def __repr__(self):
        return f"{self.NAME} {self.REGION}"

class LESSON(BASE):
    __tablename__ = "Lesson"
    ID = Column(Integer, primary_key=True)
    NAME = Column(NVARCHAR(20))
    RATE = Column(Integer)
    notes = relationship("NOTES", back_populates="lesson")

    def __init__(self, NAME: str, RATE: int):
        self.NAME = NAME
        self.RATE = RATE

    def __repr__(self):
        return f"{self.NAME} {self.RATE}"

class TEACHER(BASE):
    __tablename__ = "Teacher"
    ID = Column(Integer, primary_key=True)
    NAME = Column(NVARCHAR(20))
    SURNAME = Column(NVARCHAR(20))
    notes = relationship("NOTES", back_populates="teacher")

    def __init__(self, NAME: str, SURNAME: str):
        self.NAME = NAME
        self.SURNAME = SURNAME

    def __repr__(self):
        return f"{self.NAME} {self.SURNAME}"

class NOTES(BASE):
    __tablename__ = "Notes"
    ID = Column(Integer, primary_key=True)
    STUDENT = Column(Integer, ForeignKey("Student.ID"))
    LESSON = Column(Integer, ForeignKey("Lesson.ID"))
    MIDTERM = Column(Integer)
    FINAL = Column(Integer)
    TEACHER = Column(Integer, ForeignKey("Teacher.ID"))
    CITY = Column(Integer, ForeignKey("City.ID"))
    
    student = relationship("STUDENT", back_populates="notes")
    lesson = relationship("LESSON", back_populates="notes")
    teacher = relationship("TEACHER", back_populates="notes")
    city = relationship("CITY")

    def __init__(self, STUDENT: int, LESSON: int, MIDTERM: int, FINAL: int, TEACHER: int, CITY: int):
        self.STUDENT = STUDENT
        self.LESSON = LESSON
        self.MIDTERM = MIDTERM
        self.FINAL = FINAL
        self.TEACHER = TEACHER
        self.CITY = CITY
    
    def __repr__(self):
        return f"Notes(STUDENT={self.STUDENT}, LESSON={self.LESSON}, MIDTERM={self.MIDTERM}, FINAL={self.FINAL}, TEACHER={self.TEACHER}, CITY={self.CITY})"

def create_session():
    """
    Create session for database.
    """
    engine = create_engine("mssql+pyodbc://@localhost/sqlalchemyDB?driver=ODBC+Driver+17+for+SQL+Server", echo=True)
    BASE.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def add_student(session, name: str, surname: str):
    new_student = STUDENT(NAME=name, SURNAME=surname)
    session.add(new_student)
    session.commit()
    print(f"Added student: {new_student}")

def add_city(session, name: str, region: str):
    new_city = CITY(NAME=name, REGION=region)
    session.add(new_city)
    session.commit()
    print(f"Added city: {new_city}")

def add_lesson(session, name: str, rate: int):
    new_lesson = LESSON(NAME=name, RATE=rate)
    session.add(new_lesson)
    session.commit()
    print(f"Added lesson: {new_lesson}")

def add_teacher(session, name: str, surname: str):
    new_teacher = TEACHER(NAME=name, SURNAME=surname)
    session.add(new_teacher)
    session.commit()
    print(f"Added teacher: {new_teacher}")

def add_notes(session, student_id: int, lesson_id: int, midterm: int, final: int, teacher_id: int, city_id: int):
    new_notes = NOTES(STUDENT=student_id, LESSON=lesson_id, MIDTERM=midterm, FINAL=final, TEACHER=teacher_id, CITY=city_id)
    session.add(new_notes)
    session.commit()
    print(f"Added notes: {new_notes}")

def get_all_students(session):
    students = session.query(STUDENT).all()
    for student in students:
        print(student)

def get_student_by_id(session, student_id: int):
    student = session.query(STUDENT).get(student_id)
    if student:
        print(student)
    else:
        print(f"No student found with ID: {student_id}")

def update_student(session, student_id: int, name: str = None, surname: str = None):
    student = session.query(STUDENT).get(student_id)
    if student:
        if name:
            student.NAME = name
        if surname:
            student.SURNAME = surname
        session.commit()
        print(f"Updated student: {student}")
    else:
        print(f"No student found with ID: {student_id}")

def delete_student(session, student_id: int):
    student = session.query(STUDENT).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted student with ID: {student_id}")
    else:
        print(f"No student found with ID: {student_id}")

def get_student_notes(session, student_id: int):
    student = session.query(STUDENT).options(joinedload(STUDENT.notes)).filter(STUDENT.ID == student_id).one_or_none()
    if student:
        for note in student.notes:
            print(note)
    else:
        print(f"No student found with ID: {student_id}")

def get_teacher_students(session, teacher_id: int):
    notes = session.query(NOTES).filter(NOTES.TEACHER == teacher_id).all()
    student_ids = set(note.STUDENT for note in notes)
    students = session.query(STUDENT).filter(STUDENT.ID.in_(student_ids)).all()
    for student in students:
        print(student)

def get_average_scores(session):
    results = session.query(
        NOTES.LESSON,
        func.avg(NOTES.MIDTERM).label("avg_midterm"),
        func.avg(NOTES.FINAL).label("avg_final")
    ).group_by(NOTES.LESSON).all()
    for lesson_id, avg_midterm, avg_final in results:
        lesson = session.query(LESSON).get(lesson_id)
        print(f"Lesson: {lesson.NAME}, Avg Midterm: {avg_midterm}, Avg Final: {avg_final}")

def transaction_example(session):
    try:
        student1 = STUDENT(NAME="Transaction", SURNAME="Test1")
        student2 = STUDENT(NAME="Transaction", SURNAME="Test2")
        session.add(student1)
        session.add(student2)
        session.commit()
        print("Transaction successful")
    except Exception as e:
        session.rollback()
        print(f"Transaction failed: {e}")

if __name__ == "__main__":
    session = create_session()
    # Test functions
    add_student(session, "Serkan", "YASAR")
    add_city(session, "Istanbul", "Marmara")
    add_lesson(session, "Mathematics", 5)
    add_teacher(session, "MERT", "YILDIZ")
    add_notes(session, 1, 1, 85, 90, 1, 1)
    get_all_students(session)
    get_student_by_id(session, 1)
    update_student(session, 1, name="Serkan")
    delete_student(session, 1)
    add_student(session, "Ali", "Veli")
    add_student(session, "Ayşe", "Fatma")
    add_teacher(session, "Ahmet", "Mehmet")
    add_lesson(session, "FIZIK", 4)
    add_notes(session, 2, 2, 78, 88, 2, 1)
    add_notes(session, 3, 2, 65, 75, 2, 1)
    get_student_notes(session, 2)
    get_teacher_students(session, 2)
    get_average_scores(session)
    transaction_example(session)
