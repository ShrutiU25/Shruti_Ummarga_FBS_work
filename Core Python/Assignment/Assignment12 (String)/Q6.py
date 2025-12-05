#Q6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

def replace_hyphen(text):
    return text.replace(" ", "-")

s = input("Enter a string: ")
print("Changed string:", replace_hyphen(s))
