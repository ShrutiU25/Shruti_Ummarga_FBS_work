#Q8. Python Program to Remove the Characters of Odd Index Values in a String

def remove_odd(text):
    return text[0::2]

s = input("Enter a string: ")
print("Changed string:", remove_odd(s))
