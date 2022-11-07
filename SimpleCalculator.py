# Python program to make a simple calculator
# take 1st input and save in the variable as a floating point number
# to restrict input to only numbers and put in a loop
while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Please input a valid number: ")
    # choose the operation you want to perform
print("Operations: addition (+), Subtraction (-), multiplication (*), Division (/)")
operation = input("Select an operation: ")

# to reject wrong mathematical symbols input
while operation not in ['+', '*', '/', '-']:
    print("Invalid Operation")
    operation = input("Select a valid operation: ")

# to get a valid input for 2nd number and reject invalid number
while True:
    try:
        num2 = float(input("Enter the Second number: "))
        break
    except ValueError:
        print("Please input a valid number: ")

        # for addition(+)

if operation == "+":
    print(num1, "+", num2, "=", num1 + num2)

# for subtraction(-)
elif operation == "-":
    print(num1, "-", num2, "=", num1 - num2)

# for multiplication(*)
elif operation == "*":
    print(num1, "*", num2, "=", num1 * num2)
# for division(/)
elif operation == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    # for division(/)
    print(num1, "/", num2, "=", num1 / num2)
