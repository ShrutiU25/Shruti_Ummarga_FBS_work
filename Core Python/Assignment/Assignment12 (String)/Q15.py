# 15. Python Program to find larger string using built-in functions.

def length(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    return len1 , len2

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

ans = length(str1,str2)

if(ans[0] > ans[1]):
    print("Largest string is string 1:", ans[0] )
else:
    print("Largest string is string 2:", ans[1] )
    
