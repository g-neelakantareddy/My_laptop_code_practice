#  flatten list
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


if __name__ == "__main__":
    list_of_numbers = [2, 4, [45, 54, [34, 66], 43, 47], 23, 76]
    if list_of_numbers:
        print(flatten_list(list_of_numbers))
    else:
        print("Invalid input")
