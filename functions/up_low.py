"""
Write a Python function that accepts a string and calculate
the number of upper case letters and lower case letters.
"""

def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1

    print(s)
    print("Upper case character: ", d["upper"])
    print("Lower case character: ", d["lower"])

def main():
    up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

if __name__ == "__main__":
    main()
