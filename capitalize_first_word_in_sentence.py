def capitalize_first_letter(sentence):
    capitalize_list = []
    split_string = sentence.split()

    for word in split_string:
        capital_word = word.capitalize()
        capitalize_list.append(capital_word)

        joined_list = " ".join(capitalize_list)
    return joined_list


if __name__ == "__main__":
    while True:
        try:
            sentence_string = input("Write a sentence:").strip().lower()
            if sentence_string:
                print(capitalize_first_letter(sentence_string))
                break
            else:
                print("Don't leave empty")
        except ValueError as e:
            print("An error occurred as", e)