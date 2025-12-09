#Q4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

def square_dict(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i * i
    return d

print(square_dict(5))   
