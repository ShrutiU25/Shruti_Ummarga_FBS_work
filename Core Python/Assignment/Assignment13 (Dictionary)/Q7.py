#Q7. Python Program to Remove the Given Key from a Dictionary

def remove_key(d, key):
    if(key in d):
        del d[key]
    return d

d = {"a": 1, "b": 2, "c": 3}
print(remove_key(d, "b"))
