from linked_list import LinkedList


def main():

    ll = LinkedList()

    print("Initial size: ", len(ll))
    ll.push(10)
    ll.push(12)
    ll.push(14)
    ll.push(15)
    ll.push(10)
    print("Print list: ", ll)
    print("Delete 10")
    ll.delete(10)
    print("Print list: ", ll)
    print("New size: ", len(ll))
    print("Print list: ", ll)
    print("Push 2 elements")
    ll.push(30)
    ll.push(23)
    print("New size: ", len(ll))
    print("Print list: ", ll)
    ll.pop()
    print("New size: ", len(ll))
    print("Print list: ", ll)
    print("List contains 123? ", ll.contains(123))
    ll.append(123)
    print("New size: ", len(ll))
    print("Print list: ", ll)
    print("List contains 123? ", ll.contains(123))
    print("Delete 14")
    ll.delete(14)
    print("Print list: ", ll)


if __name__ == "__main__":
    main()
