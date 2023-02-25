import pymongo
from classes import DATA, Dataprocess,DBMongo,Students,Courses,Careers

def main():
    client, db = DBMongo.getDB()
    pipeline = Dataprocess(DATA)
    
    Students.delete_all(db)
    Careers.delete_all(db)
    Courses.delete_all(db)

    pipeline.create_courses(db)
    pipeline.create_careers(db)
    pipeline.create_students(db)
    pipeline.create_enrollments()
    client.close()

    return True
if __name__ == "__main__":
    main()