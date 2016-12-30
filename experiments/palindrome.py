"""Write a function that checks if a given sentence is a palindrome."""

import string

def is_palindrome(word):
    new_text = ''
    for char in word.lower():
        if char in string.ascii_letters:
            new_text += char

    if new_text == new_text[::-1]:
        return True
    else:
        return False

def main():
    print("Noel sees Leon is palindrome? ", is_palindrome("Noel sees Leon."))

if __name__ == "__main__":
    main()
