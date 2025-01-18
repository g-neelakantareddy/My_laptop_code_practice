#find count_vowels in sentence or paragraph
def count_vowels(txt):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in txt:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    while True:
        try:
            txt = input("Write something to find how many vowels presented in it:").strip().lower()
            if txt:
                if txt.isdigit():
                    print("Write only in characters to count vowels")
                else:
                    print(count_vowels(txt))
                    break
            else:
                print("Don't leave empty, write something")
        except Exception as e:
            print("An error occurred", e)