#A function to enter the number of students
def num_students():
    a = int(input('Please enter the number of students: '))
    return a

#A function to enter student info based on the number of students
def student_info(num_student, listStudent):
    for i in range(num_student):
        print('Enter information of student ' + (i + 1))
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
    for course in listCourse:
        if course['name'] == nameCourse:
            continue
        else: 
            print("The course does not exist!")
            return
    for student in listStudent:
        score = float(input("Enter the score of the student: "))
        student["f{nameCourse}"] = score





