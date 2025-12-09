#Q8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

def word_freq(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

s = "python is easy and python is powerful"
print(word_freq(s))
