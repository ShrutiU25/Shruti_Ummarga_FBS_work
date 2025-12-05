#Q11. Python Program to replace every blank space with hyphen in a string.

def replace_hyphen(text):
    return text.replace(" ", "-")

s = input("Enter a string: ")
print("Changed string:", replace_hyphen(s))
