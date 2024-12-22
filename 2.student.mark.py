class Student: 
    numStudent = 0
    listStudent = []
    #Define the constructor
    def __init__ (self, name, id, DoB): 
        self.__name = name
        self.__id = id
        self.__DoB = DoB
        Student.numStudent += 1
        Student.listStudent.append(self) #Keeping track of all students in the school! (Maybe a school class would be needed soon)
        self.__course = [] #Why do we need this: So that in the future, we can calculate Student's GPA!

    def __str__(self):
        return f"Student: {self.__name}, ID: {self.__id}, DoB: {self.__DoB}"
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

    def addCourse(self, course): #
        self.__course.append({f"Course": course})
    
    def enterScore(self, course, score): 
        for Course in self.__course: 
            if Course["Course"] == course: 
                Course["Score"] = score
                break
            else:
                continue

    def showScore(self):
        for Course in self.__course:
            print(f"The score of {Course['Course']} of {self.getName()} is {Course['Score']}")

    @staticmethod
    def listAllStudent():
        for Person in Student.listStudent:
            print(Person)
            Person.showScore()




class Course: 
    courseNumber = 0
    listCourse = []

    def __init__(self, name, ID, listStudent):
        self.__name = name
        self.__ID = ID
        self.__listStudent = listStudent
        Course.courseNumber += 1
        Course.listCourse.append(self)

    def __str__(self):
        return f"Course name: {self.__name}, ID: {self.__ID}"

    def setName (self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setID (self, id):
        self.__ID = id
    
    def getID(self):
        return self.__ID
    
    # def enrollStudent(self, listStudent):
    #     self.__listStudent = listStudent

    def enterScore(self):
        for Student in self.__listStudent: 
            score = float(input(f"Please enter the score of {Student.getName()} for {self.getName()}: "))
            Student.addCourse(self.getName())
            Student.enterScore(self.getName(), score)

    @staticmethod
    def listAllCourse():
        for subject in Course.listCourse:
            print(subject)


def num_students():
    a = int(input('Please enter the number of students: '))
    return a

def num_courses(): 
    num_courses = int(input('Please enter the number of courses: '))
    return num_courses

NCMT = Student("Manh Thang", "23BI14403", "19/06/2005")
HanLe = Student("Han Le Sy", "23BI14403", "31/12/2005")
Ngoc = Student("Ngoc", "23BI12345", "12/3/2005")
a = num_courses()

for i in range(a):
    courseName = input("Enter the course name: ")
    courseID = input("Enter course ID: ")
    Course(courseName, courseID, Student.listStudent)

for course in Course.listCourse:
    course.enterScore()

Student.listAllStudent()
Course.listAllCourse()


