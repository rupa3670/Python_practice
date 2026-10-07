#problem:03
#Student Grade Calculation

def get_grade(average,marks):
    if min(marks) < 33:
        return "F"
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    elif average >= 33:
        return "D"
    else:
        return "F"
marks = []

for i in range(1,6):
    while True:
        try:
            m=float(input(f"Enter marks of subject {i}: "))
            if m < 0 or m > 100:
                print("Invalid input. Please enter a valid number between 0 and 100.")
            else:
                marks.append(m)
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
total = sum(marks)
average = total/5
grade = get_grade(average,marks)
status = "Fail" if grade == "F" else "Pass"

print(f"Total Marks:{total:g}")
print(f"AVerage Marks:{average:.2f}")
print(f"Final grade:{grade}")
print(f"Status: {status}")
