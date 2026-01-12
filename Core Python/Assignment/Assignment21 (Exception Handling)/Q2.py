#2. Create class television that has members to hold the model number ,screen size and price.
#Take a member function to take input from user, If more than 4 digits are entered for model number, 
#if screen size is smaller than 12 inches or greater than 70 inches or if the price is negative or greater than 5000 Rs,
#then throw an exception. Write a main() that instantiates an object and allows the user to enter and display data.
#If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def accept(self):
        try:
            self.model_number = int(input("Enter Model Number: "))
            if len(str(self.model_number)) > 4:
                raise ValueError("Model number must be at most 4 digits")

            self.screen_size = int(input("Enter Screen Size (in inches): "))
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches")

            self.price = float(input("Enter Price: "))
            if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0 and 5000")

        except ValueError as e:
            print("Exception caught:", e)
            # Replace all values with zero
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("Model Number:", self.model_number)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)

def main():
    tv = Television()
    tv.accept()
    tv.display()
main()

         
    