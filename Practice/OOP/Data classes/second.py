from dataclasses import dataclass, field

@dataclass
class Student:
    
    name: str
    age: int
    subjects: list[str] = field(default_factory=list)



student1 = Student("Drei", 16)
student2 = Student("Alex", 16)

student1.subjects.append("Python")

print(student1.subjects)
print(student2.subjects)