sentence = input("Enter a sentence: ")

words = sentence.split()
seen = set()
repeated = set()

for word in words:
    if word.isalpha():
        word_lower = word.lower()  # make it case-insensitive
        if word_lower in seen:
            repeated.add(word_lower)
        else:
            seen.add(word_lower)

print("Repeated words:", repeated)
print("Number of repeated words:", len(repeated))
