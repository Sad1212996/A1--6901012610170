class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}")


def read_students(filename):
    students = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, age, gpa = line.split(",")
            student = Student(name, int(age), float(gpa))
            students.append(student)
    return students


def show_all(students):
    print("---ข้อมูลนักเรียนทั้งหมด---")
    for s in students:
        s.show()


def show_youngest(students):
    youngest = students[0]
    for s in students:
        if s.age < youngest.age:
            youngest = s
    print("---นักเรียนที่อายุน้อยที่สุด---")
    youngest.show()


# ------- โปรแกรมหลัก -------
students = read_students("student.txt")
show_all(students)
show_youngest(students)