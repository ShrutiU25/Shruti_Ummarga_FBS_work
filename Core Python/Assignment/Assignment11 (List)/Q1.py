#Q1.Python Program to Put Even and Odd elements of a List into two Different Lists

def sep_even_odd(li):
    even = []
    odd = []
    for i in li:
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    return even, odd

li = [1, 2, 3, 4, 5, 6, 7, 8]
even_list, odd_list = sep_even_odd(li)

print("Even List:", even_list)
print("Odd List:", odd_list)
