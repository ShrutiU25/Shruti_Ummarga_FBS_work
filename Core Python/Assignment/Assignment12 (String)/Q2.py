#Q2. Program to Remove the nth Index Character from a Non-Empty String

def removeChar(str,n):
    return str[:n] + str[n+1:]

str = input("Enter your string: ")
n = int(input("Enter index of character to remove: "))

result = removeChar(str,n)
print(result)
