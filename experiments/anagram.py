"""An anagram is a word formed from another by rearranging its letters,
    using all the original letters exactly once;
    for example, orchestra can be rearranged into carthorse."""


def is_anagram(word_1, word_2):
    return all(char in word_1.lower().replace(" ", "") for char in word_2.lower().replace(" ", ""))


def main():
    print("orchestra and carthorse are anagram? ", is_anagram("orchestra", "carthorse"))
    print("neuralll and unrelllarrooaarr are anagram? ", is_anagram("neuralll", "unrelllarrooaarr"))
    print("bibliotecario and beato coi libri are anagram? ", is_anagram("bibliotecario", "beato coi libri"))
    print("donna and danno are anagram? ", is_anagram("donna", "danno"))
    print("danno and donna are anagram? ", is_anagram("danno", "donna"))

if __name__ == "__main__":
    main()
