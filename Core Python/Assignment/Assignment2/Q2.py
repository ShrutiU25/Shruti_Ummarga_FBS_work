#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
