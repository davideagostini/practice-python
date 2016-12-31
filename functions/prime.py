# check if a number is prime

def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False

    return prime


def main():
    number = input("Insert a number: ")
    print("{0} is prime? ".format(number), is_prime(int(number)))

if __name__ == "__main__":
    main()
