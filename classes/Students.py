class Students:
    def __init__(self,Objet,id=""):
        self.Objet= Objet
        
        self.__id = id
        self.__collection="Students"
    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )  

        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
    
    def find(db):
        collection = db["Students"]
        collection.find()
    
    @staticmethod
    def get_list(db):
        collection = db["Students"]
        estudiantes = collection.find()

        list_estudiantes = []
        for e in estudiantes:
            temp_estudiante = Students(    
                e["Objet"]
                , e["_id"]        
            ) 
            list_estudiantes.append(temp_estudiante)
        return list_estudiantes
    
    @staticmethod
    def delete_all(db):
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db)

#numero_cuenta,nombre_completo,cursos_aprobados,cursos_reprobados,edad,carrera