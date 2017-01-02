## count the number of vowels in a word

def count_vowels(word):
    vowels = {}
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            if c in vowels:
                count = vowels[c]
                vowels[c] = int(count) + 1
            else:
                vowels[c] = 1

    return vowels


def main():
    word = input("Insert a word:\n")
    vowels = count_vowels(word)

    for k, v in vowels.items():
        print("{0} - {1}".format(k,v))


if __name__ == "__main__":
    main()
