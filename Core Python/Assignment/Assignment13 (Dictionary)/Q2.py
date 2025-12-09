#Q2. Python Program to Concatenate Two Dictionaries Into One

def concat_dict(d1, d2):
    d1.update(d2)
    return d1

d1 = {"x": 10, "y": 20}
d2 = {"a": 1, "b": 2}
print(concat_dict(d1, d2))
