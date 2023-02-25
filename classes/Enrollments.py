from classes.data import DATA
class Enrollments:
    def __init__(self,student,course,id="") :
        self.student=student
        self.course=course
        self.__id=id
        self.__collection="Enrollments"
    ## este no guarda solo muestra


    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )  

        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

