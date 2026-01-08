#Q7. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first 
#and vice versa. Use the Python set.

def missing_numbers(a, b):
    return a - b, b - a

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(missing_numbers(A, B))   # ({1,2,3}, {6,7})
