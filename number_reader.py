total = 0
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

    total += number
    count += 1


average = total / count


print(total, count, average)

