from classes.Students import Students
from classes.Careers import Careers
from classes.Courses import Courses
from classes.data import DATA
class Dataprocess:
    def __init__(self, data):
        self.__data = data

    def create_careers(self,db):
        ## Do something to create careers on your mongodb collection using __data
        temp={}
        for i in range(len(DATA)):
            temp [i]=DATA[i]
            
            Careers(temp[i]["carrera"]).save(db)
        return True
    def create_courses(self,db):
        ## Do something to create courses on your mongodb collection using __data
        temp= {}
        curreprob={}
        curaprob={}
        for i in range(len(DATA)):
            temp [i]=DATA[i]
            curaprob[i]=temp[i]["cursos_aprobados"]
            curreprob[i]= temp[i]["cursos_reprobados"]
        
            Courses(temp[i]["cursos_aprobados"]).save(db)
            Courses(temp[i]["cursos_reprobados"]).save(db)
            
        return True
    def create_students(self,db):
        ## Do something to create students on your mongodb collection using __data
        print(type(DATA))
        #key1='numero_cuenta'
        #key2='nombre_completo'
        #key3='cursos_aprobados'
        #key4='cursos_reprobados'
        #key5='edad' 
        #key6= 'carrera'
        temp ={}
        for i in range(len(DATA)):
            temp [i]=DATA[i]
            Students(temp[i]).save(db)
            #print(temp[i]["nombre_completo"])
        return True
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        
        return True
    
    