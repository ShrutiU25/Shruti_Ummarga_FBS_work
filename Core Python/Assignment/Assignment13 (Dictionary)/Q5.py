#Q5. Python Program to Sum All the Items in a Dictionary

def sum_dict(d):
    return sum(d.values())

d = {"a": 10, "b": 20, "c": 30}
print(sum_dict(d))
