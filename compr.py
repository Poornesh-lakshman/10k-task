def separate_vowels_consonants(text):
    vowels = ""
    consonants = ""

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += ch
            else:
                consonants += ch

    print("Vowels     :", vowels)
    print("Consonants :", consonants)

string = "hi hello raju"
separate_vowels_consonants(string)