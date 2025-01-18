# Write a program that calculates the factorial of a given number.


number = int(input("Enter a number: ").strip())
factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(factorial)
