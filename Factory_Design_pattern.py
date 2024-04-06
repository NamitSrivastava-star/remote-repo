"""
Factory Design Pattern Code
"""
from abc import ABCMeta, abstractstaticmethod

class Person(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method(self):
        """
        abstract method
        """

class Student(Person):
    def __init__(self, student_name=None):
        self.student_name = student_name

    def person_method(self):
        print(f"Student Name is {self.student_name}")            

class Teacher(Person):
    def __init__(self, teacher_name=None):
        self.teacher_name = teacher_name

    def person_method(self):
        print(f"Teacher Name is {self.teacher_name}")

class PersonFactory():
    @staticmethod
    def buildPerson(person_type, person_name):
        if person_type == "Student":
            return Student(person_name)
        elif person_type == "Teacher":
            return Teacher(person_name)
        else:
            print("Invalid {person_type}, {person_name}")                            


if __name__ == "__main__":
    person_type = input("Enter which type person object you want to create ")
    person_name = input("Enter the name of the person ")
    person = PersonFactory.buildPerson(person_type=person_type, person_name=person_name) 
    person.person_method()           