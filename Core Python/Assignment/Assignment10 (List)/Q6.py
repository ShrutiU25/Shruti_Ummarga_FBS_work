#Q6. Write a program to remove duplicates from the list.

def remove_duplicates(li):
    new = []
    for i in(li):
        found = False
        for j in new:
            if(i == j):
                found = True
                break
        if(not found):
            new.append(i)
    return new

li = [2, 5, 2, 8, 5, 9, 8, 2]
print("Original list:", li)
new_list = remove_duplicates(li)
print("List without duplicates:", new_list)
