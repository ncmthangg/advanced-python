class Student: 
    numStudent = 0
    listStudent = []
    #Define the constructor
    def __init__ (self, name, id, DoB): 
        self.__name = name
        self.__id = id
        self.__DoB = DoB
        Student.numStudent += 1
        Student.listStudent.append(self)
        self.__course = []

    ##Define all the getters and setters for the instance variables
    def setName (self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setID (self, id):
        self.__id = id
    
    def getID(self):
        return self.__id

    def setDoB(self, DoB):
        self.__DoB = DoB

    def getDoB(self):
        return self._DoB

    def scoreCourse(self, course): #The 
        self.__course.append({f"Course": course})
    
    #def enterScore(self, course, score): 

    

class Course: 
    __courseNumber = 0

    def __init__(self, name, ID):
        self.__name = name
        self.__ID = ID
        self.__listStudent = []
        Course.__courseNumber += 1

    def setName (self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setID (self, id):
        self.__ID = id
    
    def getID(self):
        return self.__ID
    
    def enrollStudent(self, listStudent):
        self.__listStudent = listStudent


def num_students():
    a = int(input('Please enter the number of students: '))
    return a

def num_courses(): 
    num_courses = int(input('Please enter the number of courses: '))
    return num_courses

NCMT = Student("Manh Thang", "23BI14403", "19/06/2005")

listStudent = NCMT.listStudent
numStudent = len(NCMT.listStudent)
for i in range(numStudent):
    print(f"{listStudent[i].getName()} is in the course")

