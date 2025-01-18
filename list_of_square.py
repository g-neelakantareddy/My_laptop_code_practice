def list_square(n):
    list_of_square = []
    for i in range(1, n + 1):
        num = i * i
        list_of_square.append(num)
    return list_of_square


if __name__ == "__main__":
    number = int(input("Enter a number: ").strip())
    for i in list_square(number):
        print(i)
