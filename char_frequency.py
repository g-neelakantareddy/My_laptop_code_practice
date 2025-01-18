def char_freq(txt):
    frequency = {}
    for char in txt:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


if __name__ == "__main__":
    while True:
        txt = input("write a sentence: ").strip()
        if txt:
            print(char_freq(txt))
            break
        else:
            print("Please valid sentence")