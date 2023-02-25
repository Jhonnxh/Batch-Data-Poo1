class Careers:
    def __init__(self,name, id="") :
        self.name=name
        self.__id=id
        self.__collection="Careers"

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
        collection = db["Careers"]
        careers_collection = collection.find()

        list_careers = []
        for e in careers_collection:
            temp_careers = Careers(    
                e["name"]
                , e["_id"]        
            ) 
            list_careers.append(temp_careers)
        return list_careers
    
    @staticmethod
    def delete_all(db):
        lista_e = Careers.get_list(db)
        for e in lista_e:
            e.delete(db)