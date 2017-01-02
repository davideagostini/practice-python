"""
return a list consisting of the largest number from each provided sub-list
"""

def main():
    my_list = [[4,5,1,3], [13,27,18,26], [32,35,37,39], [1000,1001,851,1]]
    print("Start list is: ", my_list)

    end_list = [ max(x) for x in my_list ] #list comprehensions

    print("The largest number of each sub-list are: ", end_list)


if __name__ == "__main__":
    main()
