"""
Markbook Application
Group members: Herbert, Jaywon, Emad, Alex
"""
# All work has been done by the people who committed unless otherwise stated
from typing import Dict, List
import json

# List of all classroom dictionaries
classrooms = []

# First menu interface of the program 
def main():
    while True:
        print()
        print('        Markbook        ')
        print('------------------------')
        print('[1] Create Classroom')
        print('[2] List All Classrooms')
        print('[3] Exit Program')
        print()
        
        choice = valid_int_input('Choose Menu Option: ')

        if choice == 1:
            menu_create_classroom()
        elif choice == 2:
            list_classroom()
        elif choice == 3:
            print()
            print('Thank you for using Markbook!')
            quit()
        else:
            print()
            print('Please choose a valid menu option.')


# Checks to see if the user's input is an integer
def valid_int_input(str: str) -> int:
    while True:
        try:
            integer = int(input(str))
        except ValueError:
            print('Invalid Input. Please Enter a Number.')
        else:
            return integer


# Creates a UI for the teacher to create a classroom
def menu_create_classroom():
    print()
    print('Enter the class information')
    print()
    course_code = input('Enter course code: ')
    course_name = input('Enter course name: ')
    period = valid_int_input('Enter period number: ')
    teacher = input('Enter teacher name: ')
    classroom = create_classroom(course_code, course_name, period, teacher)
    classrooms.append(classroom)
    print()
    print('Classroom created successfully')
    return None

# classroom_option and list_classroom are Jaywon's functions
# Lists all classrooms
def list_classroom():
    print()
    print(' List of all Classrooms ')
    print('------------------------')
    if classrooms == []:
        print('No Classrooms Have Been Added.')
        print()
        print('Returning to main menu...')
    else:
        index = 0
        for classroom in classrooms:
            print(f'{index}. {classroom["course_name"]}')
            index += 1
        print ()
        while True:
            user_input = valid_int_input("Enter Class Number: ") 
            if user_input < len(classrooms):
                temp_room = classrooms[user_input]
                classroom_options(temp_room)
                return None
            else:
                print('Classroom does not exist.')

# Creates menu of classroom options
def classroom_options(classroom: Dict):
    while True:
        print()
        print(f'Classroom: {classroom["course_name"]}     ')
        print('------------------------')
        print('[1] View / Edit List Of Students:')
        print('[2] View / Edit List Of Assignments:')
        print('[3] Add Student')
        print('[4] Create Assignment')
        print('[5] Save Classroom to File')
        print('[6] Return to Main Menu:')
        print()
        
        user_input = valid_int_input("Choose Menu Option: ")
        
        if user_input == 1:
            lst_student = classroom['student_list']
            # passes a lst_student to the function
            menu_student_list(lst_student, classroom)
        elif user_input == 2:
            lst_assignment = classroom['assignment_list']
            # pass a lst_assignment to the function
            menu_assignment_list(lst_assignment)
        elif user_input == 3:
            menu_add_student(classroom)
        elif user_input == 4:
            menu_create_assignment(classroom)
        elif user_input == 5:
            save_file(classroom)
        elif user_input == 6:
            return None
        else:
            ('Please choose a valid menu option.')

# Prints list of students
def menu_student_list(students: List, classroom: Dict):
    print()
    print('  List of all Students ')
    print('------------------------')
    if students == []:
        print('No Students Have Been Added.')
        print()
        print('Returning to classroom menu...')
        return None
    else:
        index = 0
        for student in students:
            print(f'{index}. {student["first_name"]} {student["last_name"]}')
            index += 1
        print ()
        while True:
            user_input = valid_int_input("Enter Student Number: ") 
            if user_input < len(students):
                temp_stu = students[user_input]
                student_options(temp_stu, classroom)
                return None
            else:
                print('Student does not exist.')

# list out all assignments in a classroom
def menu_assignment_list(assignments: List):
    print()
    print('List of all Assignments ')
    print('------------------------')
    if assignments == []:
        print('No Assignments Have Been Added.')
        print()
        print('Returning to classroom menu...')
        return None
    else:
        index = 0
        for assignment in assignments:
            print(f'{index}. {assignment["name"]}')
            index += 1
        print ()
        while True:
            user_input = valid_int_input("Enter Assignment Number: ") 
            if user_input < len(assignments):
                temp_assign = assignments[user_input]
                view_assignment(temp_assign)
                return None
            else:
                print('Assignment does not exist.')

# User Interface to create a student
def menu_add_student(classroom: Dict):
    print()
    print("Enter the student's information")
    print()
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    student_number = valid_int_input("Student Number: ")
    grade = valid_int_input("Grade: ")
    email = input("Email: ")
    print ('Hit enter after inputing all marks')
    marks_input = input('Marks: ')
    marks = [int(mark) for mark in marks_input.split()]
    temp_student = create_student(first_name, last_name, 
    student_number, grade, email, marks)
    add_student_to_classroom(temp_student, classroom)
    print()
    print('Student added successfully.')
    print()
    return None

# Creates student dictionary
def create_student(first_name: str, last_name: str, student_number: int,
grade: int, email: str, marks: List):
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'student_number': student_number,
        'grade': grade,
        'email': email,
        'marks': marks
    }

    return student

# user interface to create assignment
def menu_create_assignment(classroom: Dict):
    print()
    print("Enter the assignment information")
    print()
    name = input("Assignment Name: ")
    due = input("Due Date: ")
    points = valid_int_input("Points: ")
    temp_assign = create_assignment(name, due, points)
    classroom['assignment_list'].append(temp_assign)
    print()
    print('Assignment added successfully.')
    print()
    return None

# student_options is Qingfeng's (Alex's) function
# user interface to interact with student information
def student_options(student: Dict, classroom: Dict):
    while True:
        print()
        print(f'Student: {student["first_name"]} {student["last_name"]}')
        print('------------------------')
        print('[1] View Student Information')
        print('[2] Remove Student')
        print('[3] Calculate Average Mark')
        print('[4] Return to Classroom Menu')
        print()

        user_input = valid_int_input("Choose Menu Option: ")

        if user_input == 1:
            menu_view_stu_info(student)
        elif user_input == 2:
            remove_student_from_classroom(student, classroom)
            print (f'Successfully removed {student["first_name"]} {student["last_name"]} from classroom')
            return None
        elif user_input == 3:
            menu_calculate_average(student)
        elif user_input == 4:
            print('Returning to classroom menu...')
            return None
        else:
            ('Please choose a valid menu option.')    

# shows a student's info
def menu_view_stu_info(student: Dict):
    print(f'First Name: {student["first_name"]}')
    print(f'Last Name: {student["last_name"]}')
    print(f'Student Number: {student["student_number"]}')
    print(f'Grade: {student["grade"]}')
    print(f'Email: {student["email"]}')
    print(f'Marks: {student["marks"]}')
    print()
    input('Hit enter to return to classroom menu')
    return None

# checks if marks is empty and calculates average mark
def menu_calculate_average(student: Dict):
    if student['marks'] == []:
        print ()
        print (f'{student["first_name"]} {student["last_name"]} has no marks inputted')
        return None
    else:
        average = calculate_average_mark(student)
        print ()
        print (f"{student['first_name']} {student['last_name']}'s average mark is {average}")
        return None

# prints all assignment information
def view_assignment(assignment: Dict):
    print()
    print(f'Name: {assignment["name"]}')
    print(f'Due Date: {assignment["due"]}')
    print(f'Points: {assignment["points"]}')
    print()
    input('Hit enter to return to classroom menu')
    return None


# saves classrooms to a .txt file
def save_file(classroom: Dict):
    with open(classroom["course_name"]+".txt", "w") as write_file:
        json.dump(classroom, write_file)
    print('File successfully saved')
    return None

# Creates assignment
def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    assignment = {
        'name': name,
        'due': due,
        'points': points
    }

    return assignment

# creates classroom
def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
        'course_code': course_code,
        'course_name': course_name,
        'period': period,
        'teacher': teacher,
        'student_list': [],
        'assignment_list': [],
        
    }

    return classroom 

# calculates student's average
def calculate_average_mark(student: Dict) -> float:
    sum = 0
    marks = student['marks']
    for num in marks:
        sum += num

    average = sum/len(marks)
    
    return average

# adds student to classroom
def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append(student)
    
# removes student from classroom
def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom["student_list"].remove(student)

# edits student info
def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    for key, value in kwargs.items():
        student[key] = value
    
    pass

if __name__ == "__main__":
    main()
