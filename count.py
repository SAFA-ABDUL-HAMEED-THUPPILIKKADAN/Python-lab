s = input("Enter a string: ")

countVowels = 0
countConsonants = 0
checked = set()        # to avoid counting repeated chars again

vowels = "AEIOUaeiou"

for letter in s:
    if letter.isalpha():     # ignore spaces, numbers, symbols
        if letter not in checked:
            if letter in vowels:
                countVowels += 1
            else:
                countConsonants += 1

            checked.add(letter)

print("Vowels:", countVowels)
print("Consonants:", countConsonants)
