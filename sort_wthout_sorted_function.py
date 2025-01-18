# Sorting without using sort method or sorted func

def sorting(nums):
    length = len(nums)
    for i in range(length):
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if __name__ == "__main__":
    while True:
        try:
            numbers = input("Enter numbers by given ',':").strip()
            if numbers:
                numbers = [int(num) for num in numbers.split(",")]
                print(numbers)
                print(sorting(numbers))
                break
            else:
                print("don't leave empty space, enter numbers by given space each number")
        except:
            print("An error")
