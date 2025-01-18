import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter a number: ").strip())
    if is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is not not prime number")
