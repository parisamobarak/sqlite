from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import schemas,models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/RegStu/',response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db:Session=Depends(get_db)):
    db_student=db.query(models.Student).filter(models.Student.ids ==student.ids).first()
    if db_student:
        raise HTTPException(status_code=400,detail='already exists')
    student=models.Student(fname=student.fname,lname=student.lname,father=student.father,birth=student.birth,ids=student.ids,borncity=student.borncity,addres=student.addres,postalcode=student.postalcode,cphone=student.cphone,hphone=student.hphone,department=student.department,major=student.major,married=student.married,scourseids=student.scourseids,lids=student.lids,id=student.id,stid=student.stid)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get('/RegStu/{student_stid}',response_model=schemas.StudentRead)
def read_student(student_stid:int,db:Session=Depends(get_db)):
    db_student=db.query(models.Student).filter(models.Student.stid ==student_stid).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail='STUDENT NOT FOUND')
    return db_student



@app.delete('/DelStu/{student_stid}')
def delete_student(student_stid: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.stid == student_stid).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail='STUDENT NOT FOUND')
    db.delete(db_student)
    db.commit()
    return {"message": f"Student with stid {student_stid} has been deleted."}





@app.post('/UpStu/{student_stid}', response_model=schemas.Student)
def update_student(student_stid: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.stid == student_stid).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # تنظیم مستقیم فیلدها از اطلاعات جدید دانشجو
    db_student.fname = student.fname
    db_student.lname = student.lname
    db_student.father = student.father
    db_student.birth = student.birth
    db_student.ids = student.ids
    db_student.borncity = student.borncity
    db_student.addres = student.addres
    db_student.postalcode = student.postalcode
    db_student.cphone = student.cphone
    db_student.hphone = student.hphone
    db_student.department = student.department
    db_student.major = student.major
    db_student.married = student.married
    db_student.scourseids = student.scourseids
    db_student.lids = student.lids
    db_student.id = student.id

    # ذخیره تغییرات در پایگاه داده
    db.commit()

    # بازخوانی دانشجو برای به‌روزرسانی اطلاعات
    db.refresh(db_student)

    return db_student








@app.post('/RegTeach/',response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db:Session=Depends(get_db)):
    db_teacher=db.query(models.Teacher).filter(models.Teacher.id ==teacher.id).first()
    if db_teacher:
        raise HTTPException(status_code=400,detail='already exists')
    teacher=models.Teacher(fname=teacher.fname,lname=teacher.lname,birth=teacher.birth,borncity=teacher.borncity,addres=teacher.addres,postalcode=teacher.postalcode,cphone=teacher.cphone,hphone=teacher.hphone,department=teacher.department,major=teacher.major,lcourseid=teacher.lcourseid,id=teacher.id,lid=teacher.lid)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher



@app.get('/RegTeach/{teacher_lid}',response_model=schemas.TeacherRead)
def read_teacher(teacher_lid:int,db:Session=Depends(get_db)):
    db_teacher=db.query(models.Teacher).filter(models.Teacher.lid ==teacher_lid).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail='TEACHER NOT FOUND')
    return db_teacher


@app.delete('/DelTeach/{teacher_lid}')
def delete_teacher(teacher_lid: int, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.lid == teacher_lid).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail='TECHER NOT FOUND')
    db.delete(db_teacher)
    db.commit()
    return {"message": f"teacher with lid {teacher_lid} has been deleted."}



@app.post('/UpTeach/{teacher_lid}', response_model=schemas.Teacher)
def update_teacher(teacher_lid: int, teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.lid == teacher_lid).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")

    # تنظیم مستقیم فیلدها از اطلاعات جدید استاد
    db_teacher.fname = teacher.fname
    db_teacher.lname = teacher.lname
    db_teacher.birth =teacher.birth
    db_teacher.borncity = teacher.borncity
    db_teacher.addres = teacher.addres
    db_teacher.postalcode = teacher.postalcode
    db_teacher.cphone = teacher.cphone
    db_teacher.hphone = teacher.hphone
    db_teacher.department = teacher.department
    db_teacher.major = teacher.major
    db_teacher.lcourseid = teacher.lcourseid
    db_teacher.id = teacher.id

    # ذخیره تغییرات در پایگاه داده
    db.commit()

    # بازخوانی استاد برای به‌روزرسانی اطلاعات
    db.refresh(db_teacher)

    return db_teacher




@app.post('/RegLes/', response_model=schemas.Lesson)
def create_lesson(lesson: schemas.LessonCreate, db: Session = Depends(get_db)):
    db_lesson = db.query(models.Lesson).filter(models.Lesson.cid == lesson.cid).first()
    if db_lesson:
        raise HTTPException(status_code=400, detail='already exists')
    lesson = models.Lesson(cname=lesson.cname,part=lesson.part,credit=lesson.credit, cid=lesson.cid)
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson

@app.get('/RegLes/{lesson_cid}',response_model=schemas.LessonRead)
def read_lesson(lesson_cid:int,db:Session=Depends(get_db)):
    db_lesson=db.query(models.Lesson).filter(models.Lesson.cid ==lesson_cid).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail='LESSON NOT FOUND')
    return db_lesson

@app.delete('/DelLes/{lesson_cid}')
def delete_lesson(lesson_cid: int, db: Session = Depends(get_db)):
    db_lesson = db.query(models.Lesson).filter(models.Lesson.cid == lesson_cid).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail='STUDENT NOT FOUND')
    db.delete(db_lesson)
    db.commit()
    return {"message": f"lesson with stid {lesson_cid} has been deleted."}

@app.post('/UpLes/{lesson_cid}', response_model=schemas.Lesson)
def update_lesson(lesson_cid: int, lesson: schemas.LessonCreate, db: Session = Depends(get_db)):
    db_lesson = db.query(models.Lesson).filter(models.Lesson.cid == lesson_cid).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    db_lesson.cname = lesson.cname
    db_lesson.part = lesson.part
    db_lesson.credit = lesson.credit
    db_lesson.cid = lesson.cid

    db.commit()
    db.refresh(db_lesson)
    return db_lesson





