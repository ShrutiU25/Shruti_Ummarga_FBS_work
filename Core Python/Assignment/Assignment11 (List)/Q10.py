#Q10. Write a program to print list after removing even numbers 

def remove_even(num):
    result = []
    for i in num:
        if(i % 2 != 0):
            result.append(i)
    return result

num = [10, 13, 24, 37, 41, 56, 67]

print("Original list :", num)
print("After removing even numbers:", remove_even(num))
