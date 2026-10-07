#Name:Rupali Akter
#ID:23
#problem:02
#Number Classification

def classify(number):
    if number > 0:
        number_type = "Positive"
    elif number < 0:
        number_type = "Negative"
    else:
        number_type= "Zero"
    return{
        "Number type": number_type,
        "Parity": "Even" if number % 2 == 0 else "Odd",
        "Divided by 5 and 7": "Yes" if number % 35 == 0 else "No",
        "Two_Digit Number":"Yes" if 10 <= abs(number) <= 99 else "No"
    }
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
            print("Invalid input. Please enter a valid number.")

for key, value in classify(number).items():
    print(f"{key}: {value}")