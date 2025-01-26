def remove_white_spaces(sentence):
    split_string = sentence.split()
    no_spaces_string = "".join(split_string)
    return no_spaces_string


if __name__ == "__main__":
    while True:
        try:
            sentence_with_spaces = input("Write a sentence with spaces: ").strip().lower()
            if sentence_with_spaces:
                print(remove_white_spaces(sentence_with_spaces))
                break
            else:
                print("Dont leave empty write something")
        except Exception as e:
            print("An error occurred", e)
