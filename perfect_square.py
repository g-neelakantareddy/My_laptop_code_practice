import math

"""
isqrt() will return only the integer square root of a number (not a float). If squaring that integer equals the 
original input number, then the number is a perfect square.
"""


def perfect_square(num):
    if num < 0:
        return False
    else:
        square_root = math.isqrt(num)
        return square_root * square_root == num


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter a number: ").strip())
            if number:
                if perfect_square(number):
                    print(f"{number} is a perfect square")
                    break
                else:
                    print(f"{number} not a perfect square number")
                    break
            else:
                print("Don't leave empty")
        except ValueError as e:
            print("Invalid input", e)
