#Q1.Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook

class Book:
    def __init__(self, bid = None, bname = None, price = None, author = None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object created")

    def getData(self):
        display = f"Book id = {self.bid} \nBook name = {self.bname} \nBook price = {self.price}\nNook author = {self.author}"
        return display 
    
    def __del__(self):
        print("Book object deleted")
    
c1 = Book(1, "ABC", 200, "Ram")
print(c1.getData())

c2 = Book()
print(c2.getData())


