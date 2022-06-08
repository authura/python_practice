total = 0
count = 0

while True:
    n_string = input("Enter a number: ")

    try:
        float(n_string)
    except:
        print("Invalid input. Please enter a number.")

