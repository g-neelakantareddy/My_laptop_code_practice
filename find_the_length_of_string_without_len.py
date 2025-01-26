#  We are removing white spaces and finding the length
def len_of_String(words):
    count = 0
    split_string = words.split()
    joined_string = "".join(split_string)
    for char in joined_string:
        count += 1
    return count


if __name__ == "__main__":
    while True:
        try:
            string = input("Write something you like: ").strip().lower()
            if string:
                print(len_of_String(string))
                break
            else:
                print("Don't leave empty")
        except Exception as e:
            print("An error occurred", e)