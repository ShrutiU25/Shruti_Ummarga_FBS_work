#Q2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook

class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created")

    def ShowProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def __del__(self):
        print("Product object deleted")

p1 = Product(201, "Mobile", 15000, 2)
p1.ShowProduct()
