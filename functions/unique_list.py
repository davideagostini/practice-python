"""Write a Python function that takes a list and
returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""

def unique_list(l):
    ll = []
    for x in l:
        if x not in ll:
            ll.append(x)
    return ll


def main():
    print("Sample list: ", [1,1,1,1,2,2,3,3,3,3,4,5])
    print("Unique list: ", unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

if __name__ == "__main__":
    main()
