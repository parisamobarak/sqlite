from database import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = 'student'

    stid = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    father = Column(String)
    birth = Column(String)
    ids = Column(String, unique=True)
    borncity = Column(String)
    addres = Column(String)
    postalcode = Column(Integer)
    cphone = Column(Integer)
    hphone = Column(Integer)
    department = Column(String)
    major = Column(String)
    married = Column(String)
    id = Column(Integer, unique=True)
    scourseids = Column(Integer)
    lids = Column(Integer)
class Teacher(Base):
    __tablename__ = 'teacher'

    lid = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    id = Column(Integer, unique=True)
    department = Column(String)
    major = Column(String)
    birth = Column(String)
    borncity = Column(String)
    addres = Column(String)
    postalcode = Column(Integer)
    cphone =Column(Integer)
    hphone =Column(Integer)
    lcourseid =Column(Integer)

class Lesson(Base):
    __tablename__ = 'lesson'

    cid= Column(Integer, primary_key=True, index=True)
    part=Column(String)
    cname = Column(String)
    credit = Column(Integer)
