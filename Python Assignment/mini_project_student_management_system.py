#Name:Rupali Akter
#ID:23
#Problem:15
#Mini Project - Student Result Management System

import json
import math
from pathlib import Path


DATA_FILE = Path(__file__).with_name("student_results.json")
SUBJECT_COUNT = 5


def read_nonempty(prompt):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("Error: This field cannot be empty.")


def read_mark(subject_number, current_mark=None):
	while True:
		value = input(f"Enter Subject {subject_number} Marks" +
					  (" (press Enter to keep current): " if current_mark is not None else ": ")).strip()
		if not value and current_mark is not None:
			return current_mark
		if not value:
			print("Invalid marks! Please enter a value from 0 to 100.")
			continue
		try:
			mark = float(value)
			if math.isfinite(mark) and 0 <= mark <= 100:
				return mark
			print("Invalid marks! Marks must be between 0 and 100.")
		except ValueError:
			print("Invalid marks! Please enter a number from 0 to 100.")


def calculate_result(student):
	marks = student["marks"]
	student["total_marks"] = sum(marks)
	student["average_marks"] = student["total_marks"] / SUBJECT_COUNT

	# The student fails if any subject mark is below 33.
	failed_subject = False
	for mark in marks:
		if mark < 33:
			failed_subject = True
			break

	if failed_subject:
		student["grade"] = "F"
		student["status"] = "Fail"
	else:
		average = student["average_marks"]
		if average >= 80:
			student["grade"] = "A+"
		elif average >= 70:
			student["grade"] = "A"
		elif average >= 60:
			student["grade"] = "A-"
		elif average >= 50:
			student["grade"] = "B"
		elif average >= 40:
			student["grade"] = "C"
		else:
			student["grade"] = "D"
		student["status"] = "Pass"


def find_student_index(students, student_id):
	for index, student in enumerate(students):
		if student["student_id"] == student_id:
			return index
	return -1


def add_student(students):
	student_id = read_nonempty("Enter Student ID: ")
	if find_student_index(students, student_id) != -1:
		print("Error: That Student ID already exists.")
		return

	name = read_nonempty("Enter Name: ")
	department = read_nonempty("Enter Department: ")
	marks = []
	for subject_number in range(1, SUBJECT_COUNT + 1):
		marks.append(read_mark(subject_number))

	student = {
		"student_id": student_id,
		"name": name,
		"department": department,
		"marks": marks,
	}
	calculate_result(student)
	students.append(student)
	print("Student added successfully.")


def print_student_table(students):
	if not students:
		print("No student records to display.")
		return

	headers = ["Student ID", "Name", "Department"]
	headers.extend(f"Sub {number}" for number in range(1, SUBJECT_COUNT + 1))
	headers.extend(["Total", "Average", "Grade", "Status"])
	rows = []
	for student in students:
		row = [student["student_id"], student["name"], student["department"]]
		row.extend(f"{mark:g}" for mark in student["marks"])
		row.extend([
			f"{student['total_marks']:g}",
			f"{student['average_marks']:.2f}",
			student["grade"],
			student["status"],
		])
		rows.append(row)

	widths = []
	for column_number in range(len(headers)):
		column_width = len(headers[column_number])
		for row in rows:
			if len(row[column_number]) > column_width:
				column_width = len(row[column_number])
		widths.append(column_width)

	def format_row(values):
		return " | ".join(value.ljust(widths[index]) for index, value in enumerate(values))

	print(format_row(headers))
	print("-+-".join("-" * width for width in widths))
	for row in rows:
		print(format_row(row))


def view_all_students(students):
	print_student_table(students)


def search_student(students):
	student_id = read_nonempty("Enter Student ID to search: ")
	index = find_student_index(students, student_id)
	if index == -1:
		print("Student not found.")
		return
	print_student_table([students[index]])


def calculate_student_result(students):
	student_id = read_nonempty("Enter Student ID to calculate result: ")
	index = find_student_index(students, student_id)
	if index == -1:
		print("Student not found.")
		return
	student = students[index]
	calculate_result(student)
	print_student_table([student])


def update_student(students):
	student_id = read_nonempty("Enter Student ID to update: ")
	index = find_student_index(students, student_id)
	if index == -1:
		print("Student not found.")
		return

	student = students[index]
	print("Press Enter to keep the current value.")
	name = input(f"Name [{student['name']}]: ").strip()
	if name:
		student["name"] = name
	department = input(f"Department [{student['department']}]: ").strip()
	if department:
		student["department"] = department
	updated_marks = []
	for subject_number in range(1, SUBJECT_COUNT + 1):
		current_mark = student["marks"][subject_number - 1]
		updated_mark = read_mark(subject_number, current_mark)
		updated_marks.append(updated_mark)
	student["marks"] = updated_marks
	calculate_result(student)
	print("Student record updated successfully.")


def delete_student(students):
	student_id = read_nonempty("Enter Student ID to delete: ")
	index = find_student_index(students, student_id)
	if index == -1:
		print("Student not found.")
		return
	del students[index]
	print("Student record deleted successfully.")


def class_statistics(students):
	if not students:
		print("No student records available for statistics.")
		return

	total_of_averages = 0
	highest_average = students[0]["average_marks"]
	lowest_average = students[0]["average_marks"]
	highest_total = students[0]["total_marks"]
	passed_students = 0
	top_students = []

	for student in students:
		average = student["average_marks"]
		total_of_averages += average
		if average > highest_average:
			highest_average = average
		if average < lowest_average:
			lowest_average = average
		if student["total_marks"] > highest_total:
			highest_total = student["total_marks"]
			top_students = [student]
		elif student["total_marks"] == highest_total:
			top_students.append(student)
		if student["status"] == "Pass":
			passed_students += 1

	class_average = total_of_averages / len(students)
	failed_students = len(students) - passed_students

	print(f"Total number of students: {len(students)}")
	print(f"Class average: {class_average:.2f}")
	print(f"Highest average: {highest_average:.2f}")
	print(f"Lowest average: {lowest_average:.2f}")
	print(f"Passed students: {passed_students}")
	print(f"Failed students: {failed_students}")
	print("Highest-scoring student(s):")
	print_student_table(top_students)


def save_data(students):
	try:
		with DATA_FILE.open("w", encoding="utf-8") as file:
			json.dump(students, file, indent=2, ensure_ascii=False)
		print(f"Saved {len(students)} student record(s) to {DATA_FILE.name}.")
		return True
	except OSError as error:
		print(f"Error: Could not save student data: {error}")
		return False


def load_data(show_message=True):
	try:
		with DATA_FILE.open("r", encoding="utf-8") as file:
			saved_students = json.load(file)
		if not isinstance(saved_students, list):
			raise ValueError("The data file must contain a list of student records.")

		students = []
		seen_ids = set()
		for saved_student in saved_students:
			if not isinstance(saved_student, dict):
				raise ValueError("A student record is not in the expected format.")
			student_id = saved_student.get("student_id")
			name = saved_student.get("name")
			department = saved_student.get("department")
			marks = saved_student.get("marks")
			if (not isinstance(student_id, str) or not student_id.strip()
					or not isinstance(name, str) or not name.strip()
					or not isinstance(department, str) or not department.strip()
					or not isinstance(marks, list) or len(marks) != SUBJECT_COUNT):
				raise ValueError("A student record has missing or invalid fields.")
			if student_id in seen_ids:
				raise ValueError(f"Duplicate Student ID in data file: {student_id}")

			checked_marks = []
			for mark in marks:
				if isinstance(mark, bool) or not isinstance(mark, (int, float)):
					raise ValueError(f"Invalid marks found for Student ID {student_id}.")
				if not math.isfinite(mark) or not 0 <= mark <= 100:
					raise ValueError(f"Marks out of range for Student ID {student_id}.")
				checked_marks.append(float(mark))

			student = {
				"student_id": student_id,
				"name": name,
				"department": department,
				"marks": checked_marks,
			}
			calculate_result(student)
			students.append(student)
			seen_ids.add(student_id)

		if show_message:
			print(f"Loaded {len(students)} student record(s).")
		return students
	except FileNotFoundError:
		if show_message:
			print("No saved data file was found.")
		return []
	except (OSError, json.JSONDecodeError, ValueError, TypeError) as error:
		if show_message:
			print(f"Error: Could not load student data: {error}")
		return None


def display_menu():
	print("\n========================================")
	print("STUDENT RESULT MANAGEMENT")
	print("========================================")
	print("1. Add Student")
	print("2. View All Students")
	print("3. Search Student")
	print("4. Calculate Result")
	print("5. Update Student")
	print("6. Delete Student")
	print("7. Class Statistics")
	print("8. Save Data")
	print("9. Load Data")
	print("10. Exit")


def main():
	students = load_data(show_message=False)
	if students is None:
		print("Saved data could not be loaded. Starting with an empty student list.")
		students = []

	while True:
		display_menu()
		choice = input("Select an option: ").strip()

		if choice == "1":
			add_student(students)
		elif choice == "2":
			view_all_students(students)
		elif choice == "3":
			search_student(students)
		elif choice == "4":
			calculate_student_result(students)
		elif choice == "5":
			update_student(students)
		elif choice == "6":
			delete_student(students)
		elif choice == "7":
			class_statistics(students)
		elif choice == "8":
			save_data(students)
		elif choice == "9":
            if not DATA_FILE.exists():
                print("No saved data file was found.")
            else:
                loaded_students = load_data()
                if loaded_students is not None:
                    students = loaded_students
		elif choice == "10":
			save_data(students)
			print("Student Result Management System closed safely.")
			break
		else:
			print("Error: Select a menu option from 1 to 10.")


if __name__ == "__main__":
	try:
		main()
	except (EOFError, KeyboardInterrupt):
		print("\nInput interrupted. Exiting safely.")
