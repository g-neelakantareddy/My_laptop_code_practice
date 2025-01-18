sentence = "Create a simple calculator that performs addition, subtraction, multiplication, and division"
words = sentence.split()
largest = 0
for i in words:
    word_len = len(i)
    if word_len > largest:
        largest = word_len
for j in words:
    if largest == len(j):
        print(j)

"""clean_words = [word.strip(",") for word in words]
largest = max(len(word) for word in clean_words)

largest_word = [word for word in clean_words if len(word) == largest]
print(str(largest_word))"""

