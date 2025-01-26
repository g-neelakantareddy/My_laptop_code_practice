def sub_string(word_1, word_2):
    if word_2 in word_1:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        try:
            string_1 = input("Write big word or sentence: ").strip().lower()
            string_2 = input("Write another word to check word in above word / sentence: ").strip().lower()
            if string_1 and string_2:
                if sub_string(string_1, string_2):
                    print(f"Yes its correct, {string_2} in {string_1}")
                    break
                else:
                    print(f"No sorry its not correct, {string_2} not in {string_1}")
                    break
            else:
                print("Don't leave empty write something to achieve")
        except Exception as e:
            print("An error occurred", e)
