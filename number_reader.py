total = 0
count = 0

while True:
    n_string = input("Enter a number: ")

    if n_string == "done":
        break
    
    try:
        n = float(n_string)
    except:
        print("Invalid input. Please enter a number.")
        continue
    
    total = total + n
    count = count + 1


