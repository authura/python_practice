#Ask for the total bill
# convert input to float
# ask how many are spitting the bill
# convert input to float
# ask how much they want to tip
# total bill = total *.0{percent}, then total + tip

print("Welcome to the tip calculator\n\n")

subtotal = float(input("Please enter total bill\n\n"))

split = int(input("How many people are splitting the bill?\n\n"))

tip = int(input("How much in % would you like to tip?\n\n"))

total = tip / 100 * subtotal + subtotal

individual_total = total / split

print(f"Each individual should pay {individual_total}")