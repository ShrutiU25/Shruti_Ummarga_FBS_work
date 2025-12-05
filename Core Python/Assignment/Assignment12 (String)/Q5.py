#Q5. Python Program to Count the Number of Vowels in a String

def vowels(str):
    v = ["a", "e", "i", "o", "u"]
    found = []
    count = 0
    for i in str :
        if(i in v):
            found.append(i)
    count = len(found)       
    return found, count

str = input("Enter string : ")
ans = vowels(str)

print("Vowels found:", ans[0])
print("Number of vowels:", ans[1])