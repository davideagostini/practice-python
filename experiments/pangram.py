# Write a function or method to check a sentence to see if it is a pangram (or not)
# A pangram is a sentence that contains all the letters of the English alphabet at least once.
# For example, the quick brown fox jumps over the lazy dog.


from string import ascii_lowercase

#ver 1
def is_pangram(text):
    return all(char in text.lower() for char in ascii_lowercase)

#ver 2
def is_pangram_2(text):
    for char in ascii_lowercase:
        if char not in text.lower():
            return False
    return True


def main():
    current = True
    while current:
        text = input("Write a text (0 to exit): ")
        if text == '0':
            current = False
        else:
            result = is_pangram_2(text)
            if result:
                print("The text: " + text + " is a pangram")
            else:
                print("Ops, isn't a pangram")

if __name__ == "__main__":
    main()
