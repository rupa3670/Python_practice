#Name:Rupali Akter
#ID:23
#Problem:11
#Student Management System Using Dictionary

import math


def read_nonempty(prompt):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("Error: This field cannot be empty.")


def read_cgpa():
	while True:
		try:
			cgpa = float(input("Enter CGPA: "))
			if math.isfinite(cgpa) and cgpa >= 0:
				return cgpa
			print("Error: CGPA must be a finite, non-negative number.")
		except ValueError:
			print("Error: Enter a valid number for CGPA.")


def add_student(students):
	student_id = read_nonempty("Enter student ID: ")
	if student_id in students:
		print("Error: A student with that ID already exists.")
		return

	students[student_id] = {
		"Name": read_nonempty("Enter student name: "),
		"Department": read_nonempty("Enter department: "),
		"CGPA": read_cgpa(),
	}
	print("Student added successfully.")


def search_student(students):
	student_id = read_nonempty("Enter student ID to search: ")
	student = students.get(student_id)
	if student is None:
		print("Student not found.")
		return

	print(f"Student ID: {student_id}")
	for detail, value in student.items():
		print(f"{detail}: {value}")


def display_students(students):
	if not students:
		print("No student records to display.")
		return

	for student_id, student in students.items():
		print(f"\nStudent ID: {student_id}")
		for detail, value in student.items():
			print(f"{detail}: {value}")


def update_cgpa(students):
	student_id = read_nonempty("Enter student ID to update: ")
	if student_id not in students:
		print("Student not found.")
		return

	students[student_id]["CGPA"] = read_cgpa()
	print("CGPA updated successfully.")


def delete_student(students):
	student_id = read_nonempty("Enter student ID to delete: ")
	if student_id in students:
		del students[student_id]
		print("Student deleted successfully.")
	else:
		print("Student not found.")


def main():
	students = {}

	while True:
		print("\nStudent Management System")
		print("1. Add Student")
		print("2. Search Student")
		print("3. Display All Students")
		print("4. Update CGPA")
		print("5. Delete Student")
		print("6. Exit")
		choice = input("Select an option: ").strip()

		if choice == "1":
			add_student(students)
		elif choice == "2":
			search_student(students)
		elif choice == "3":
			display_students(students)
		elif choice == "4":
			update_cgpa(students)
		elif choice == "5":
			delete_student(students)
		elif choice == "6":
			print("Exiting Student Management System.")
			break
		else:
			print("Error: Select a number from 1 to 6.")


if __name__ == "__main__":
	main()
