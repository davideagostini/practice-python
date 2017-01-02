# sum all the prime numbers up to and including the provided number

def sum_all_prime(n):
    count = 0
    for i in range(2,n+1):
        if is_prime(i):
            count += i

    return count


def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False

    return prime


def main():
    number = input("Insert a number: ")
    print("The sum of all prime numbers is", sum_all_prime(int(number)))

if __name__ == "__main__":
    main()
