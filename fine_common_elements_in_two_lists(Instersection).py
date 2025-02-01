def instersection_lists(list_1, list_2):
    common_items = []
    for item in list_1:
        if item in list_2:
            common_items.append(item)
    return common_items


if __name__ == "__main__":
    first_list = [2, 4, 6, 7, 34, 65, 76, 86]
    second_list = [4, 6, 8, 43, 65, 6]
    result = instersection_lists(first_list, second_list)
    print(f"Comments in both lists {result}")