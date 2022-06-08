
count = 0

while True:
    string = input("Enter a number: ")
    
    if string == "done":
        break
        
    
    try:
        number = float(string)

    except:
        print("Invalid input.")

        continue

    if count == 0:

        minimum = number
        maximum = number

    elif number < minimum:
        minimum = number

    elif number > maximum:
        maximum = number

        
    count += 1


print(minimum, maximum)