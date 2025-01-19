def second_largest_number(numbers):
    largest_number = float("-inf")
    second_largest_num = 0
    for num in numbers:
        if num > largest_number:
            second_largest_num = largest_number
            largest_number = num
        elif num > second_largest_num and num != largest_number:
            second_largest_num = num
    return second_largest_num


if __name__ == "__main__":
    while True:
        numbers = input('Enter numbers given by \',\': ').strip()
        if numbers:
            numbers = [int(num) for num in numbers.split(",")]
            print(second_largest_number(numbers))
            break
        else:
            print("Don't leave empty")
