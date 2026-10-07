#Name:Rupali Akter
#Student ID:23
#Problem:08
# String Analyzer

def string_analyzer(sentence):
	alphabets = digits = spaces = vowels = consonants = upper = lower = 0

	for ch in sentence:
		if ch.isalpha():
			alphabets += 1
			if ch.lower() in "aeiou":
				vowels += 1
			else:
				consonants += 1
			if ch.isupper():
				upper += 1
			elif ch.islower():
				lower += 1
		elif ch.isdigit():
			digits += 1
		elif ch == " ":
			spaces += 1

	return {
		"Total Characters": len(sentence),
		"Alphabets": alphabets,
		"Digits": digits,
		"Spaces": spaces,
		"Vowels": vowels,
		"Consonants": consonants,
		"Uppercase Letters": upper,
		"Lowercase Letters": lower,
	}


while True:
	sentence = input("Enter a sentence: ")
	if sentence.strip():
		break
	print("Error: Input cannot be empty.")

analysis = string_analyzer(sentence)
for label, count in analysis.items():
	print(f"{label}: {count}")

