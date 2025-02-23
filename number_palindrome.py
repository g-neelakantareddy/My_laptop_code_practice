# number palindrome
def number_palindrome(nums):
    numbers_in_list = [int(num) for num in nums]
    reversed_nums = numbers_in_list[::-1]
    return numbers_in_list == reversed_nums


if __name__ == "__main__":
    while True:
        try:
            numbers = input("Enters numbers :").strip()
            if numbers:
                result = number_palindrome(numbers)
                print(f"Given numbers are {result}")
                break
            else:
                print("Don't leave empty")
        except:
            print("An error occurred")
