def reverse_list(list_nums):
    reversed_list = []
    for item in list_nums:
        reversed_list.insert(0, item)
    return reversed_list


if __name__ == "__main__":
    list_numbers = [1, 2, 3, 4]
    result = reverse_list(list_numbers)
    print(f"Reversed list {result}")
