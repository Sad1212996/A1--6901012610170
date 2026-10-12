class Student:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        return f"\n แสดงข้อมูล \n name: {self.name} \n price: {self.price} บาท \n quantity: จำนวนสินค้า {self.quantity} ชิ้น\n"

student1 = Student("Anpha", 5446, 654)
student2 = Student("beta", 15645, 123445)

print(student1.show()) 
print(student2.show())  

