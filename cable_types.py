a_pins = [1, 2, 3, 4, 5, 6, 7, 8]

straight_through = [1, 2, 3, 4, 5, 6, 7, 8]

crossover = [3, 6, 1, 4, 5, 2, 7, 8]

cable = input("Pinout for which type of cable? Straight-through, crossover, or rollover:\n").lower()

if cable == 'straight-through':
    print("Straight-through Pin Pairs:")
    for i in zip(a_pins, straight_through):
        print(i)

elif cable == 'crossover':
    print("Crossover Pin Pairs:")
    for i in zip(a_pins, crossover):
        print(i)
elif cable == 'rollover':
    print("Rollover Pin Pairs:")
    straight_through.reverse()
    for i in zip(a_pins, straight_through):
        print(i)