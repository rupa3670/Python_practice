#problem:09
# Palindrome and String Reverse

sentence = input("Enter a string: ")
reversed_sentence = sentence[::-1]
normalized_sentence = "".join(sentence.split()).casefold()

print(f"Reversed String: {reversed_sentence}")
if normalized_sentence == normalized_sentence[::-1]:
	print("Palindrome: Yes")
else:
	print("Palindrome: No")

