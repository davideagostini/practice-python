
def array_test():

    array = [2,4,7,9,5]

    print("Append 5")
    array.append(5)
    print(array)

    print("Pop")
    array.pop()
    print(array)

    print("Index of 4: ", array.index(4))  # index of given value

    array.remove(7) # remove item with given value
    print("Removed 7: ", array)

    array.reverse()
    print("reversed: ", array)
    print("sorted return: ", sorted(array))

    array.sort()
    print("sorted in place: ", array)


def main():
    array_test()

if __name__ == "__main__":
    main()
