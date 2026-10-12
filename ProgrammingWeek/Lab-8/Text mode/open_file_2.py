class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        print(f"Name: {self.name}, Price: {self.price} bath, Quantity: {self.quantity} \n ราคารวมกับจำนวนสินค้า: {self.price*self.quantity} bath")


def read_students(filename):
    products = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, price, quantity = line.split(",")
            product = Product(name, int(price), int(quantity))
            products.append(product)
    return products


def show_all(products):
    print("---ข้อมูลสินค้าทั้งหมด---")
    for s in products:
        s.show()



# ------- โปรแกรมหลัก -------
products = read_students("product.txt")
show_all(products)