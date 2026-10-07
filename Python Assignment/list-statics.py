#Name:Rupali Akter
#ID:23
#Problem:10
#List Statistics

def analyze_numbers(numbers):
	largest = numbers[0]
	smallest = numbers[0]
	total = 0
	even_numbers = []
	odd_numbers = []

	# Calculate maximum, minimum, and sum manually as required.
	for number in numbers:
		if number > largest:
			largest = number
		if number < smallest:
			smallest = number
		total += number

		if number % 2 == 0:
			even_numbers.append(number)
		else:
			odd_numbers.append(number)

	duplicate_numbers = []
	for index in range(len(numbers)):
		for later_index in range(index + 1, len(numbers)):
			if numbers[index] == numbers[later_index] and numbers[index] not in duplicate_numbers:
				duplicate_numbers.append(numbers[index])

	ascending_numbers = sorted(numbers)
	descending_numbers = ascending_numbers[::-1]

	return {
		"Maximum": largest,
		"Minimum": smallest,
		"Sum": total,
		"Average": total / len(numbers),
		"Even numbers": even_numbers,
		"Odd numbers": odd_numbers,
		"Duplicate values": duplicate_numbers,
		"Ascending order": ascending_numbers,
		"Descending order": descending_numbers,
	}


while True:
	try:
		number_count = int(input("How many integers will you enter? "))
		if number_count > 0:
			break
		print("Error: Enter a number greater than zero.")
	except ValueError:
		print("Error: Enter a valid integer.")

numbers = []
while len(numbers) < number_count:
	try:
		number = int(input(f"Enter integer {len(numbers) + 1}: "))
		numbers.append(number)
	except ValueError:
		print("Error: Enter a valid integer.")

results = analyze_numbers(numbers)
print(f"List: {numbers}")
for label, value in results.items():
	print(f"{label}: {value}")
