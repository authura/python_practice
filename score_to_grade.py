def compute_grade(score):
    if score > 1 or score < 0:
        print("Input out of range.")
        quit()
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade


try:

    score = float(input("Enter score between 0.0 and 1.0:\n"))

    grade = compute_grade(score)

    print(f"Grade: {grade}")

except:

    print("Invalid input.")
