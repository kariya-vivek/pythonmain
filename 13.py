from collections import Counter

with open("file.txt", "r") as f:
    text = f.read()
    freq = Counter(text)
    print(freq)
