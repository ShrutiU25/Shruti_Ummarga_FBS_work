#Q8. Write a program to create a duplicate of an existing list. It should not point to same list.

def duplicate_list(li):
    new_list = []
    for i in li:
        new_list.append(i)
    return new_list

li = [5, 10, 15, 20]
copied_list = duplicate_list(li)

print("Original list:", li)
print("Duplicate list:", copied_list)

print("Same memory location?" , li is copied_list)   

