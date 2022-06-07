fahrenheit = input("Enter degrees in Fahrenheit: ")

#Python follows order of operations so long as parentheses are used
celsius = (float(fahrenheit) - 32) * (5/9)

print(f"Degrees in Celsius: {celsius}")
