from abc import ABC, abstractmethod


# Abstract class
class Role(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def perform_duty(self):
        pass


class Student(Role):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade   # encapsulation

    def introduce(self):
        return f"Hi, I am {self.name} and I am a student."

    def perform_duty(self):
        return f"{self.name} studies and completes assignments."

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


class Teacher(Role):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Hi, I am {self.name} and I am a teacher."

    def perform_duty(self):
        return f"{self.name} teaches {self.subject}."

class Principal(Role):
    def __init__(self,name, age):
        super().__init__(name, age)

    def introduce(self):
        return f"Hi, I am {self.name} and I the Principal."
    
    def perform_duty(self):
        return f"{self.name} manages the school."

people = [
    Student("Aqua", 14, 95),
    Teacher("Mr. Cruz", 35, "Mathematics"),
    Student("Paulo", 14, 90),
    Principal("Mr Kalbotado", "45")
]

for person in people:
    print(person.introduce())
    print(person.perform_duty())
    print()