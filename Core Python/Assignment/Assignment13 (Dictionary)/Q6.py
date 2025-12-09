#Q6. Python Program to Multiply All the Items in a Dictionary

def mul_dict(d):
    result = 1
    for value in d.values():
        result *= value
    return result

d = {"a": 2, "b": 3, "c": 4}
print(mul_dict(d))
