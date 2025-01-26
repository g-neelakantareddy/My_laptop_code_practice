def count_even_odd_nums(numbers):
    count_even = 0
    count_odd = 0
    numbers = [int(num) for num in numbers.split(",")]
    for num in numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


if __name__ == "__main__":
    while True:
        try:
            nums = input('Write numbers give by \',\' for each num:').strip()
            if nums:
                even, odd = (count_even_odd_nums(nums))
                print(f"Even nums in string {even}, Odd nums in string {odd}")
                break
            else:
                print("Don't give leave empty")
        except Exception as e:
            print("An error occurred", e)