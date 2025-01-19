# Sum of Digits
def sum_of_digits(numbers):
    result = 0
    numbers = [int(digit) for digit in str(numbers)]
    for NUM in numbers:
        assert isinstance(NUM, object)  # new learning
        result = result + NUM
    return result


if __name__ == "__main__":
    while True:
        try:
            num = input("Enter a number: ").strip()
            if num:
                if num.isdigit():
                    print(sum_of_digits(num))
                    break
                else:
                    print("Enter only numbers")
            else:
                print("Don't leave it empty")
        except ValueError:
            print("Something went wrong")