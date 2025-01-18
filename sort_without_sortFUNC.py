numbers = [3, 43, 35, 45, 75, 87, 32]
length = len(numbers)

for i in range(length):
    for j in range(0, length-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)