#Q10. Write a program to remove all occurrences of a given element in the list.

def remove_all_occurrences(li, element):
    new_list = []
    for i in li:
        if(i != element):
            new_list.append(i)
    return new_list

li = [4, 2, 4, 6, 4, 7, 4, 9]
print("Original list:", li)

num = int(input("Enter the element to remove: "))
result = remove_all_occurrences(li, num)

print(f"List after removing all occurrences of {num} :", result)


            
        
   
    
    