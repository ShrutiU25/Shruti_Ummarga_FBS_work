#Q3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

class Shirt:
    def __init__(self, sid, sname, type, price, size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print("Shirt object created")

    def ShowShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)

    def __del__(self):
        print("Shirt object deleted")    

#s1 = Shirt()
#s1.ShowShirt()
#print()

s2 = Shirt(301, "Peter England", "Formal", 1200, "Large")
s2.ShowShirt()
