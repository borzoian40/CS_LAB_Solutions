"""
04.1.7 Words and spaces. Write a program reading a word and showing all its substring, sorted by 
increasing length. If the user inputs the string 'rum', the program shall output:
r 
u 
m 
ru 
um 
rum

"""

def main(words):
    for i in range(1, len(words) + 1):
        print(words[i - 1])
    for j in range(1, len(words)):
        for k in range(1, len(words)):
            if (k + j <= len(words)):
                print(words[k - 1:k + j:1])


if __name__ == "__main__":
    words = input("Please enter your word: ")
    main(words)
