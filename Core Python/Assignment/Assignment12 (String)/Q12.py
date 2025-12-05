#Q12. Python Program to count number of lowercase characters in a string.

def countLowercase(text):
    count = 0
    for char in text:
        if(char.islower()):  
            count += 1
    return count

s = input("Enter a string: ")
print("Number of lowercase characters:", countLowercase(s))
