#Q13. Python Program to count number of digits and letters in a string.

def count_al_num(text):
    digits = 0
    letters = 0
    for char in text:
        if(char.isdigit()):      
            digits += 1
        elif(char.isalpha()):    
            letters += 1
    return digits, letters

s = input("Enter a string: ")
d, l = count_al_num(s)

print("Number of digits:", d)
print("Number of letters:", l)
