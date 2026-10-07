#Name:Rupali Akter
#ID:23
#Problem:01
#Student Information and Result Calculation
student_name = input("Name:")
student_id = input("ID:")
marks = []
count = 1
while count <= 5:  #The loop will continue until 5 valid marks are obtained.
    try:
        mark = int(input(f"Enter marks of subject {count}: "))
        marks.append(mark)
        count += 1 #Move to next subject only if the mark is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")
total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100
highest_mark = max(marks)
lowest_mark = min(marks)
print(f"Student Name: {student_name}")
print(f"Student ID: {student_id}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")

