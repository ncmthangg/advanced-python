#A function to enter the number of students
def num_students():
    a = int(input('Please enter the number of students: '))
    return a

#A function to enter student info based on the number of students
def student_info(num_student, listStudent):
    for i in range(num_student):
        print('Enter information of student ' + str(i + 1))
        name = input('Name: ')
        id = input('id: ')
        DoB = input('DoB: ')
        listStudent.append({"name": name, "id": id, "DoB": DoB})

#A function to input the number of courses
def num_courses(): 
    num_courses = int(input('Please enter the number of courses: '))
    return num_courses

#A function to input course information: id, name
def course_info(numCourses, listCourse):
    for i in range(numCourses):
        id = input('Enter the course ID: ')
        name = input('Enter course name: ')
        listCourse.append({"name": name, "id": id})

#A function to Select a course, input marks for student in this course
def input_mark(listCourse, listStudent):
    nameCourse = input("Please enter the name of the class you want to input the score: ")
    check = 0
    for course in listCourse:
        if course['name'] == nameCourse:
            check += 1
            break
        else: 
            continue

    if check == 0:
        print("The course does not exist!")
        return

    for student in listStudent:
        score = float(input("Enter the score of student " + student["name"] + ": "))
        student[nameCourse + 'score'] = score

#List all students in the course
def showStudent(listStudent):
    for student in listStudent:
        print(student)

#List all courses
def showCourses(listCourse):
    for course in listCourse:
        print(course)

#List all score in a course: 
def showScore(nameCourse, listStudent):
    for student in listStudent:
        print("The score of " + nameCourse + " of " + student["name"] + " is " + str(student[nameCourse + 'score']))

numStudent = num_students()
listStudent = []
student_info(numStudent, listStudent)
numCourse = num_courses()
listCourse = []
course_info(numCourse, listCourse)
input_mark(listCourse, listStudent)
showScore("OOP", listStudent)
