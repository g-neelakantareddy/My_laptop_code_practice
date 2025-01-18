def anagram(str_1, str_2):
    return sorted(str_1) == sorted(str_2)


if __name__ == "__main__":
    while True:
        word_1 = input("Write first word: ").strip().lower()
        word_2 = input("Write second word: ").strip().lower()
        if word_1 and word_2:
            print(anagram(word_1, word_2))
            break
        else:
            print("Don't leave empty space, Write something")
