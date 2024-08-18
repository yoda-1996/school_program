class Student:
    def __init__(self, name, age, grade_level):
        self.name = name
        self.age = age
        self.grade_level = grade_level

    def print_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade Level: {self.grade_level}")

class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def print_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")

class School:
    def __init__(self, student, teacher):
        self.student = student
        self.teacher = teacher

    def print_all_info(self):
        print("Student Information:")
        self.student.print_info()
        print("\nTeacher Information:")
        self.teacher.print_info()

student1 = Student("Owen", 15, "10th Grade")
teacher1 = Teacher("Mr.PLP", 40, "Mathematics")

school = School(student1, teacher1)

school.print_all_info()
