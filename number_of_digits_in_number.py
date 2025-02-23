# Count the Number of Digits in a Number: Write a function that counts how many digits are in a given number.
def digits_number(numbers):
    numbers_list = [int(num) for num in numbers]
    count_of_digits = 0
    for _ in numbers_list:
        count_of_digits += 1
    return count_of_digits


if __name__ == "__main__":
    while True:
        try:
            nums = input("Enter numbers:").strip()
            if nums:
                print(f"Numbers in {nums} is {digits_number(nums)}")
                break
            else:
                print("Don't leave empty")
        except ValueError as e:
            print("An error occurred as",e)