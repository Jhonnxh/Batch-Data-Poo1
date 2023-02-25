class Courses:
    def __init__(self,name,id=" ") :
        self.name=name
        self.__id=id
        self.__collection="Courses"

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )  

        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
    
    @staticmethod
    def get_list(db):
        collection = db["Courses"]
        courses = collection.find()

        list_courses = []
        for e in courses:
            temp_courses = Courses(    
                e["name"]
                , e["_id"]        
            ) 
            list_courses.append(temp_courses)
        return list_courses
    
    @staticmethod
    def delete_all(db):
        lista_e = Courses.get_list(db)
        for e in lista_e:
            e.delete(db)
    
    def savecourse(self,list_course):
        pass
