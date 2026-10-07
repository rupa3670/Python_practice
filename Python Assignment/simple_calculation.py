#Name:Rupali Akter
#Student ID:23
#Problem:04
#simple calculation

def calculator(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            return "Error: Division by zero is not allowed."
    elif operator == "%":
        if second_number != 0:
            return first_number % second_number
        else:
            return "Error: Division by zero is not allowed."
    elif operator == "**":
        return first_number ** second_number
    else:
        return first_number // second_number if second_number != 0 else "Error: Division by zero is not allowed."  

while True:
    try:
        first_number = float(input("Enter first number:"))
        break
    except ValueError:
        print("Error:Please enter a valid number")
while True:
    operator = input("Enter operator:").strip()
    if operator in ["+", "-", "*", "/", "%", "**", "//"]:
        break
    print("Error: Invalid operator. Please enter a valid operator.")
while True:
    try:
        second_number = float(input("Enter second number:"))
        break
    except ValueError:
        print("Error:Please enter a valid number")

result = calculator(first_number, second_number, operator)
if isinstance(result,str):
    print(result)
else:
    print(f"Result: {result:.1f}")