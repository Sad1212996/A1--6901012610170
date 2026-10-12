class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def show(self):
        return f"\n แสดงข้อมูล \n student_id: {self.student_id} \n name: {self.name} \n course: {self.course} \n"

student1 = Student(5464, "Anpha", "success")
student2 = Student(5464, "beta", "unsuccess")

print(student1.show()) 
print(student2.show())  