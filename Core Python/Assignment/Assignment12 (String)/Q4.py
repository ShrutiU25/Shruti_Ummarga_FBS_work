#Q4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def swap_first_last(s):
    return s[-1] + s[1:-1] + s[0]

s = input("Enter string: ")
print(swap_first_last(s))

