"""find the missing letter in the passed letter range and return it

abce -> missing letter is d

"""

from string import ascii_lowercase

def missing_letter(word):
    for i in ascii_lowercase:
        if i not in word.lower():
            return i
    else:
        return ""

def main():
    print("The missing letter in abce is: ",missing_letter("abce"))
    print("The missing letter in abcdefghjklmno is: ",missing_letter("abcdefghjklmno"))


if __name__ == '__main__':
    main()
