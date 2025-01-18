operator = input("Enter a operand (+, -, *, /) :").strip()
num1 = float(input("Enter a number:").strip())
num2 = float(input("Enter a number").strip())

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print("Invalid format")