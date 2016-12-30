# the numbers of Fibonacci

def fib(n):
    if n == 0:
         return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    number = input("Insert an int >= 0:\n")
    print("Fibonacci of {0} is {1}".format(number, fib(int(number))))

if __name__ == "__main__":
    main()
