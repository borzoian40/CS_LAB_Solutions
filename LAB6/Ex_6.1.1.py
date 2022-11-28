"""
06.1.1 Vowel Count. Write the function: 
def count_vowels(string)
that returns the number of vowels in the string. Vowels are the letters a, e, i, o, and u; as well as 
their respective capitalized versions.
"""
def countVowels(string):
    count = 0
    for i in range(len(string)):
        if (string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o"
                or string[i] == "u"
        ):
            count += 1

    print(count)


if __name__ == "__main__":
    word = input("Please enter your word: ")

    countVowels(word.lower())

