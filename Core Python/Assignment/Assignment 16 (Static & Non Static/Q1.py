#1. Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.

class Book :
    count = 0
    def __init__(self,bid=None,bname=None,author=None):
        Book.count +=1
        self.bid = bid 
        self.bname = bname
        self.author = author
        
    def showBook (self):
        data = f"book name = {self.bname}\nbook id = {self.bid}\nAuthor = {self.author}"
        return data 
         
    def __del__(self):
        print("Destructor is called ")
        
c1 = Book(1, "Wings of fire", "APJ Abdul kalam")
c2 = Book(2, "Abc", "xyz")
print("Count", Book.count)
print(c1.showBook())
        
        

        
        