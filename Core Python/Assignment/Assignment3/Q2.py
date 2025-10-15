#2. Write a program to input any alphabet and check whether it is vowel or consonant.
char = input("Enter any alphabet: ")

if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char =='O' or char =='U'):
    print(f"Character {char} is an vowel")
else:
    print(f"Character {char} is an consonant")    