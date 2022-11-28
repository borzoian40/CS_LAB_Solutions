"""
Write a function "def countWords(string)" that returns a count of all words in the string string.
Words are separated by spaces. 
For example, countWords("Mary had a little lamb") should return 5. 

"""
#First approach using SPLIT

def count_Words(input):
    print(len(input.split()))

if __name__ == "__main__":
    words = input("Please enter your word: ")
    count_Words(words)

#Second approach by counting the spaces: " " between words. And in the end adding 1.
def count_Words(string):
    count = 0
    for i in range(len(string)):
        if (string[i] == " "):
            count += 1
    print(count+1)


if __name__ == "__main__":
    word = input("Please enter your word: ")
    count_Words(word)
