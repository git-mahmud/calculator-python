print("Welcome!!")
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
operator = input("Enter an operator (+, -, ×, ÷, ^): ")

if operator == "+":
    print(f"Sum of the numbers is: {a + b}")

elif operator == "-":
    print(f"Subtraction of the numbers is: {a - b}")

elif operator == "×":
    print(f"Multiplication of the numbers is: {a * b}")

elif operator == "÷":
    if b == 0:
        print("Math error! Cannot divide by zero.")
    else:
        print(f"Division of the numbers is: {a / b}")

elif operator == "^":
    print(f"The value of a^b is: {pow(a, b)}")

else:
    print("Syntax error! Invalid operator.")