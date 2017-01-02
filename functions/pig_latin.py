"""
Pig Latin is a language game in which words in English are altered.

For words that begin with consonant sounds,
all letters before the initial vowel are placed at the end of the word sequence.
Then, "ay" is added.

For words that begin with vowel sounds, one just adds "way" to the end.
"""

def pig_latin(word):
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        print("{0}way".format(word))
    else:
        tmp = ''
        for k in word:
            if k != 'a' and k != 'e' and k != 'i' and k != 'o' and k != 'u':
                tmp += k
            else:
                break

        print("{0}{1}ay".format(word[len(tmp):], tmp))

def main():
    next_word = True
    while next_word:
        word = input("Insert a word: ")
        if word.strip():
            pig_latin(word)
        else:
            next_word = False

if __name__ == '__main__':
    main()
