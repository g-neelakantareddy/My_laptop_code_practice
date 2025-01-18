def rm_dup_from_list(list_x):
    no_duplicates = []
    duplicates = []
    for i in list_x:
        if i not in no_duplicates:
            no_duplicates.append(i)
        else:
            duplicates.append(i)

    print("List without duplicates:", no_duplicates)
    print("Duplicates found:", duplicates)


if __name__ == "__main__":
    while True:
        numbers = input("Enter a list of numbers (separated by spaces): ").strip().split()
        print(numbers)
        if numbers:
            # Convert input strings to integers
            numbers = [int(num) for num in numbers]
            rm_dup_from_list(numbers)
            break
        else:
            print("List is empty. Please enter numbers.")
