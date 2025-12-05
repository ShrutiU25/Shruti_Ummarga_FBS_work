#Q1.Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_a(text):
    return text.replace('a', '$')

s = input("Enter a string: ")
print("Changed string:", replace_a(s))
