def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 1:
        print("It is invalid")
    else:
        print(a)
        print(b)

        for i in range(2, num):
            c = a + b
            a = b
            b = c
            if c <= n:
                print(c)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    fib(num)
