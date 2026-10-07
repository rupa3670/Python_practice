#Name:Rupali Akter
#ID:23
#Problem:13
#Student Result System Using File Handling

import csv
import math
from pathlib import Path


STUDENT_FILE = Path(__file__).with_name("students.txt")


def load_students():
	students = []
	try:
		with STUDENT_FILE.open("r", newline="", encoding="utf-8") as file:
			for row in csv.reader(file):
				if len(row) != 4:
					continue
				student_id, name, department, cgpa_text = row
				try:
					cgpa = float(cgpa_text)
				except ValueError:
					continue
				if math.isfinite(cgpa):
					students.append({
						"ID": student_id,
						"Name": name,
						"Department": department,
						"CGPA": cgpa,
					})
	except FileNotFoundError:
		pass
	return students


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


def add_student():
	students = load_students()
	student_id = read_nonempty("Enter student ID: ")
	if any(student["ID"] == student_id for student in students):
		print("Error: A student with that ID already exists.")
		return

	student = {
		"ID": student_id,
		"Name": read_nonempty("Enter student name: "),
		"Department": read_nonempty("Enter department: "),
		"CGPA": read_cgpa(),
	}
	with STUDENT_FILE.open("a", newline="", encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow([
			student["ID"],
			student["Name"],
			student["Department"],
			student["CGPA"],
		])
	print("Student added successfully.")


def display_student(student):
	print(f"ID: {student['ID']}")
	print(f"Name: {student['Name']}")
	print(f"Department: {student['Department']}")
	print(f"CGPA: {student['CGPA']:.2f}")


def display_all_students():
	students = load_students()
	if not students:
		print("No student records found.")
		return

	for student in students:
		print()
		display_student(student)


def search_student():
	student_id = read_nonempty("Enter student ID to search: ")
	for student in load_students():
		if student["ID"] == student_id:
			display_student(student)
			return
	print("Student not found.")


def display_student_count():
	print(f"Total students: {len(load_students())}")


def display_highest_cgpa_student():
	students = load_students()
	if not students:
		print("No student records found.")
		return

	highest_cgpa = students[0]["CGPA"]
	for student in students[1:]:
		if student["CGPA"] > highest_cgpa:
			highest_cgpa = student["CGPA"]

	print(f"Highest CGPA: {highest_cgpa:.2f}")
	for student in students:
		if student["CGPA"] == highest_cgpa:
			display_student(student)


def main():
	while True:
		print("\nStudent Result System")
		print("1. Add a new student")
		print("2. Display all students")
		print("3. Search by student ID")
		print("4. Display total number of students")
		print("5. Display student(s) with the highest CGPA")
		print("6. Exit")
		choice = input("Select an option: ").strip()

		if choice == "1":
			add_student()
		elif choice == "2":
			display_all_students()
		elif choice == "3":
			search_student()
		elif choice == "4":
			display_student_count()
		elif choice == "5":
			display_highest_cgpa_student()
		elif choice == "6":
			print("Exiting Student Result System.")
			break
		else:
			print("Error: Select a number from 1 to 6.")


if __name__ == "__main__":
	main()
