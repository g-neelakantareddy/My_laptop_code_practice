# Write a program that finds the largest number among three numbers.
numbers = [1, 2, 3, 23, 43, 54, 3, 32, 43]
b = 0
for i in numbers:
    if i > b:
        b = i
print(b)
