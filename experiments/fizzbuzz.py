#replace any number divisible by three with the word "fizz",
#and any number divisible by five with the word "buzz"
#and any number divisible for three and five with the word "fizzbuzz"

def main():
    for i in range(1,101):
        if i % 3 == 0 & i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
