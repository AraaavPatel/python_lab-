text = input("Enter a sentence: ")

words = text.replace(".", "").split()
freq = {}

for word in words:
    word = word.capitalize()
    freq[word] = freq.get(word, 0) + 1

for key in sorted(freq):
    print(key, ":", freq[key])