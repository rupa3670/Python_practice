#Name:Rupali Akter
#Student ID:23
#Problem:07
# Prime Number and Prime Series

def is_prime(number):
    if number <2:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

while True:
    try:
        number = int(input("Enter a number: "))
        if number < 1:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

prime_numbers = [candidate for candidate in range(1, number + 1) if is_prime(candidate)]
print(f"\nPrime numbers from 1 to {number}:")
print(" ".join(map(str, prime_numbers)) if prime_numbers else "None")
print(f"Total prime numbers: {len(prime_numbers)}")

