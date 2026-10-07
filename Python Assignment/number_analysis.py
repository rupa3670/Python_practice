#Name:Rupali Akter
#Student ID:23
#Problem:06
#Number Analysis

def analyze_number(number):
    total_sum = 0
    even_sum = 0
    odd_sum = 0
    even_count = 0
    odd_count = 0
    div_3_5_count = 0

    for i in range(1, number + 1):
        total_sum += i
        if i%2 == 0:
            even_sum +=i
            even_count +=1
        else:
            odd_sum += i
            odd_count +=1
        if i % 3 == 0 and i % 5 == 0:
            div_3_5_count +=1
        
    print(f"Sum of all numbers: {total_sum}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")
    print(f"Numbers divisible by both 3 and 5: {div_3_5_count}")

while True:
    try:
        n = int(input("Enter a number: "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
analyze_number(n)