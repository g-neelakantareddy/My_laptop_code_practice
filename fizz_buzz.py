fizzbuzz = 0
fizz = 0
buzz = 0


def fizz_buzz(n):
    global fizzbuzz, fizz, buzz

    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FIZZBUZZ")
            fizzbuzz += 1
        elif num % 3 == 0:
            print("FIZZ")
            fizz += 1
        elif num % 5 == 0:
            print("BUZZ")
            buzz += 1
    print(f"{fizzbuzz},{fizz},{buzz}")


fizz_buzz(100)
