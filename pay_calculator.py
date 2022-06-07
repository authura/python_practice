
try:
    hours = float(input("Enter hours worked: "))

    rate = float(input("Enter rate: "))

#Overtime is extra hours worked * 1.5
    if hours > 40:
        pay = ((hours - 40) * rate * 1.5) + rate * 40

    else:
        pay = hours * rate

    print(f"Gross pay: {pay}\n")

except:

    print("Invalid input. Please enter a number.\n")