##6 main classes now, include: 

#A "Course" object: Course name, Course ID, Course ECTS
#   Two "sub-classes" of Course: 
#       CourseStudent (bringing the attributes of Course Score)
#       CourseUni (bringing the attributes of list of students, input grades and input student)

#A "Student" class: Most of the attributes remain the same (Would just need to copy the codes)
#Main attributes: Name, ID, DoB, List of Course (CourseStudent datatype), and GPA. 

#A "University class": Bringing the List of Students, Number of Students, List of Courses. 
#Most of the required functions of the course would be inside this class.

#An "InputInfo" class, in order to help with inputing and outputing things

#This is the InputInfo class, for elementary methods

#This is the "parent" class: Course

class Course: 
    def __init__(self, name, ID, ECTS):
        self.__name = name
        self.__ID = ID
        self.__ECTS = ECTS

    def __str__(self):
        return f"Course name: {self.__name}, ID: {self.__ID}, ECTS: {self.__ECTS}"

    #setters
    def setName (self, name):
        self.__name = name

    def setID (self, id):
        self.__ID = id

    def setECTS(self, ECTS):
        self.__ECTS = ECTS

    #getters
    def getName(self):
        return self.__name   
    
    def getID(self):
        return self.__ID

    def getECTS(self):
        return self.__ECTS


class CourseStudent(Course): 
    def __init__(self, name, id, ECTS):
        super().__init__(name, id, ECTS)
        self.__score = 0

    def setScore(self, score):
        self.__score = float(score)

    def getScore(self):
        return self.__score


class Student: 
    #Define the constructor
    def __init__ (self, name, id, DoB): 
        self.__name = name
        self.__id = id
        self.__DoB = DoB
        self.__GPA = 0
        self.__course: list[CourseStudent] = [] #Why do we need this: So that in the future, we can calculate Student's GPA!

    def __str__(self):
        return f"Student: {self.__name}, ID: {self.__id}, DoB: {self.__DoB}"
    ##Define all the getters and setters for the instance variables
    #All Setters
    def setName (self, name):
        self.__name = name
    
    def setID (self, id):
        self.__id = id

    def setDoB(self, DoB):
        self.__DoB = DoB

    #All Getters
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__id

    def getDoB(self):
        return self.__DoB

    def addCourse(self, course): #
        self.__course.append(course)
    
    def enterScore(self, coursetocheck): 
        for Course in self.__course: 
            if Course.getName() == coursetocheck: 
                Course.setScore(float(input(f"Enter the score of {Course.getName()} of {self.getName()}: ")))
                return 
        print("The student is not enrolled in the subject!")

    def calculateoverallGPA(self):
        if len(self.__course) == 0:
            print("Cannot calculate GPA for student now!")
            return
        else: 
            cumulateGPA = 0
            ECTS = 0
            for Course in self.__course:
                cumulateGPA += Course.getECTS() * Course.getScore()
                ECTS += Course.getECTS()
            self.__GPA = float(cumulateGPA) / float(ECTS)
            print(f"Overall GPA of {self.__name} is {self.__GPA}") 
        
    def showScore(self):
        for Course in self.__course:
            print(f"The score of {Course.getName()} of {self.getName()} is {Course.getScore()}")


class CourseUniversity(Course):
    def __init__(self, name, id, ECTS):
        super().__init__(name, id, ECTS)
        self.__listStudent: list[Student] = []
        self.__studentcheck = CourseStudent(name, id, ECTS)

    def enrollStudent(self, student: Student): 
        self.__listStudent.append(student)
        wtf = CourseStudent(self.getName(), self.getID(), self.getECTS())
        student.addCourse(wtf)

    def enterGPA(self):
        name = self.getName()
        for student in self.__listStudent:
            student.enterScore(name)

class InputInfo():
    @staticmethod
    def inputStudent():
        name = input("Please enter the name of the student: ")
        id = input("Please enter the Student ID: ")
        DoB = input("Please enter DoB of student: ")
        newStudent = Student(name, id, DoB)
        print(f"Finish entering information of Student {name}")
        return newStudent
    
    @staticmethod
    def inputCourse():
        name = input("Please enter the course info: ")
        id = input("Please enter the course ID: ")
        newCourse = Course(name, id)
        print(f'Finish entering information of Course {name}')
        return newCourse

class University():
    def __init__(self):
        self.__numStudent = 0
        self.__numCourses = 0
        self.__listStudent: list[Student] = []
        self.__listCourses: list[CourseUniversity] = []
    
    #getters
    def getlistCourse(self):
        return self.__listCourses

    #Functions to enter the number of courses 
    def enterNumStudent(self):
        self.__numStudent += int(input("Please enter the number of students: "))

    def enterStudentfromKeyboard(self): 
        if (self.__numStudent == 0):
            numStu = int(input("Please enter the number of students: "))
            self.__numStudent = numStu
        
        for i in range(self.__numStudent): 
            student = InputInfo.inputStudent()
            self.__listStudent.append(student)

    def enrollStudentAuto(self, listStudent):
        for student in listStudent:
            self.__listStudent.append(student)
        self.__numStudent += len(listStudent)

    def enterNumCourses(self):
        self.__numCourses += int(input("Please enter the number of courses: "))

    def enterCoursefromKeyboard(self): 
        if (self.__numCourses == 0):
            numCoursee = int(input("Please enter the number of courses: "))
            self.__numCourses = numCoursee

        for i in range(self.__numCourses):
            course = InputInfo.inputCourse()
            self.__listCourses.append(course)

    def enrollCourseAuto(self, listCourse):
        for coursenew in listCourse: 
            self.__listCourses.append(coursenew)
        self.__numStudent += len(listCourse)

    #Functions to display all Courses
    def displayCourse(self):
        for course in self.__listCourses:
            print(course)
    
    def displayStudent(self):
        for student in self.__listStudent:
            print(student)
    
    def enterScoreOneCourse(self, coursename):
        coursecheck = 0
        for course in self.__listCourses:
            if coursename == course.getName(): 
                coursecheck = course
        for student in self.__listStudent:
            coursecheck.enrollStudent(student)
        coursecheck.enterGPA()
    
    def calculateGPA(self):
        for student in self.__listStudent:
            student.calculateoverallGPA()

def defaultfunction():
    NCMT = Student("Manh Thang", "23BI14403", "19/06/2005")
    HanLe = Student("Han Le Sy", "23BI14403", "30/12/2005")
    Ngoc = Student("Ngoc", "23BI12345", "12/3/2005")
    listStudentNow = [NCMT, HanLe, Ngoc]
    DSA = CourseUniversity("DSA", "ICT.1", 3)
    OOP = CourseUniversity("OOP", "ICT.2", 4)
    listCourseNow = [DSA, OOP]

    USTH = University()
    USTH.enrollStudentAuto(listStudentNow)
    USTH.enrollCourseAuto(listCourseNow)
    USTH.displayCourse()
    USTH.displayStudent()
    USTH.enterScoreOneCourse("OOP")
    USTH.enterScoreOneCourse("DSA")
    USTH.calculateGPA()

def main():
    USTH = University()
