# Write a program that finds the largest number among three numbers.
numbers = [1, 2, 3, 23, 43, 54, 3, 32, 43]
b = 0
second_largest_number = 0
for i in numbers:
    if i > b:
        second_largest_number = b
        b = i
    elif i > second_largest_number and i != b:
        second_largest_number = i
print(second_largest_number)
