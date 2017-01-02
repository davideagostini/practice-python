"""
    The best case input is an array that is already sorted.
    In this case insertion sort has a linear running time (i.e., O(n))

    worst case and average case time (i.e., O(n**2))

"""
import logging

logging.basicConfig(filename='example.log',format='%(levelname)s:%(message)s',level=logging.DEBUG)


def sort(my_list):
    for i in range(1, len(my_list)):
        tmp = my_list[i]
        pos = i

        while pos > 0 and my_list[pos-1] > tmp:
            my_list[pos] = my_list[pos-1]
            pos -= 1

        my_list[pos] = tmp
        logging.debug("Iteration = {0}, tmp = {1}, {2}".format(i, tmp, my_list))

    return my_list


def main():
    my_list = [3,7,4,9,5,2,6,1,7,23,11]
    print("Start list is: ", my_list)
    print("Ordered list is: ", sort(my_list))


if __name__ == "__main__":
    main()
