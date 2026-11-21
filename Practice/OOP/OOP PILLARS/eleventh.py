from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def introduce(self):
        pass

class Student(Person):

    def __init__(self, names):
        self.names = names
        self.__scores = []
    
    def add_score(self, score):
        self.__scores.append(score)

    def average(self):
        if len(self.__scores) == 0:
            return 0
        return sum(self.__scores) / len(self.__scores)
    
    def is_passed(self):
        if self.average() >= 80:
            return True
        return False

    def introduce(self):
        return f"hi i am a {self.names}"

class Teacher(Person):
    def __init__ (self, names):
        self.names = names
    def give_score(self, Student, score):
        Student.add_score(score)

    def introduce(self):
        return f"hi i am {self.names} and a Teacher"

s1 = Student("Aqua")
s2 = Student("Paulo")

t1 = Teacher("Mr. Cruz")

# Teacher gives scores
t1.give_score(s1, 90)
t1.give_score(s1, 85)
t1.give_score(s2, 70)
t1.give_score(s2, 75)

# Polymorphism
people = [s1, s2, t1]

for p in people:
    print(p.introduce())

print()

# Student results
for s in [s1, s2]:
    print(s.names)
    print("Average:", round(s.average(), 2))
    print("Passed:", s.is_passed())
    print()