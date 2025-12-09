#Q3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def key_exists(d, key):
    return key in d

d = {"name": "John", "age": 25}
print(key_exists(d, "age"))   
print(key_exists(d, "salary")) 
