def compute_pay(hours, rate):
    #Overtime is extra hours worked * 1.5
    if hours > 40:
        pay = ((hours - 40) * rate * 1.5) + rate * 40

    else:
        pay = hours * rate

    return pay

try:
    hours = float(input("Enter hours worked: "))

    rate = float(input("Enter rate: "))

    #arguments in function call are not the same as the parameters
    #in function definition. These arguments are the inputs that
    #we gathered from the user input.
    pay = compute_pay(hours, rate)


    print(f"Gross pay: {pay}\n")

except:

    print("Invalid input. Please enter a number.\n")