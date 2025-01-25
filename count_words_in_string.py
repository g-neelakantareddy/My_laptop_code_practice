# Count words in a string or sentence
def count_words(string):
    count = 0
    split_words = string.split()
    for word in split_words:
        assert isinstance(word, object)
        count += 1
    return count


if __name__ == "__main__":
    while True:
        try:
            sentence = input("write something you like and find how many words are there :").strip()
            if sentence:
                print(count_words(sentence))
                break
            else:
                print("Don't leave it empty, write something and have fun")
        except:
            print("Something went wrong")
