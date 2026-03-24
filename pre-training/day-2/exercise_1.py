import string

def word_frequency(text):

    text = text.lower()

    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    return freq


paragraph = "Python is great. Python is easy to learn. Python is powerful."

result = word_frequency(paragraph)

pairs = result.items()

sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

top5 = sorted_pairs[:5]

print("Top 5 words:")
for word, count in top5:
    print(word, "-", count)
