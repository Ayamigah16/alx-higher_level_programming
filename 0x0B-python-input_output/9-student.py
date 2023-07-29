#!/usr/bin/python3
"""
Contains the clas "Student"
"""
class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with the given first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }


if __name__ == '__main__':
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
