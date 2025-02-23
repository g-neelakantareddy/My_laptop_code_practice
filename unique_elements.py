# Find the Unique Elements in a List: Write a function that returns a list of unique elements from a given list.
def unique_elements_lists(all_items):
    numbers_list = [int(num) for num in all_items]
    unique_elements = []
    for item in numbers_list:
        if numbers_list.count(item) == 1:
            unique_elements.append(item)
    return unique_elements


if __name__ == "__main__":
    while True:
        try:
            numbers = input("Enter numbers :").strip()
            if numbers:
                new_unique_items = unique_elements_lists(numbers)
                print(f"Unique elements in list {new_unique_items}")
                break
            else:
                print("Don't leave empty")
        except ValueError as e:
            print("An error occurred",e)
