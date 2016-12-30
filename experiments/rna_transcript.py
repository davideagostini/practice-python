# G -> C
# C -> G
# T -> A
# A -> U

def to_rna(dna_string):
    new_dna_string = ''
    for c in dna_string:
        if c == 'A':
            new_dna_string += 'U'
        elif c == 'G':
            new_dna_string += 'C'
        elif c == 'C':
            new_dna_string += 'G'
        else:
            new_dna_string += 'A'

    return new_dna_string


def main():
    print("First: AGCT")
    print("After: ", to_rna("AGCT"))

if __name__ == "__main__":
    main()
