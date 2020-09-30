"""
Markbook Application
Group members: 
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    Assignment = {
        'name': name,
        'due': due,
        'points': points
    }

    return Assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    Classroom = {
        'course_code': course_code,
        'course_name': course_name,
        'period': period,
        'teacher': teacher,
        'student_list': [],
        'assignment_list': [],
        
    }

    return Classroom 


def calculate_average_mark(student: Dict) -> float:
    sum = 0
    marks = student['marks']
    for num in marks:
        sum += num

    average = sum/len(marks)
    
    return average


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom["student_list"].append(student)
    

def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom["student_list"].remove(student)


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

def open_classroom(classrooms: Dict):
# assuming key of the dictionary containing all of the classrooms is classcode.
    print("List Of Classrooms")
    for classcode in classrooms:
        print(classcode)
    user_input = input("Enter the classcode: ") 
    if user_input not in classrooms:
        print('classroom does not exist')
    else:
        return classroom[input]

def classroom_options(classroom: Dict):
    print( '1. Go To The List Of Student:')
    print('2. Go To The List Of Assignment:')
    print('3. Edit Classroom Details:')
    print('4. Exit Program:')

    user_input = int(input("Enter the number: "))
    while user_input not in [1, 2, 3, 4]:
        print('wrong input')
        user_input = int(input("Enter the number: "))
        
    if user_input == 1:
        lst_student = classroom['student_list']
        # pass a lst_student to the function
    elif user_input == 2:
        lst_assignment = classroom['assignment_list']
        # pass a lst_assignment to the function
    elif user_input == 3:
        pass # optional
    elif user_input == 4:
        return classroom 
    
