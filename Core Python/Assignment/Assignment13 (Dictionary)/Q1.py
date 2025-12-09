#Q1.Python Program to Add a Key-Value Pair to the Dictionary

def add_pair(d, key, value):
    d[key] = value
    return d

d = {"a": 1, "b": 2}
print(add_pair(d, "c", 3))
