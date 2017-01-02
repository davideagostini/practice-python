def quicksort(a, start, end):
    if start < end:
        pivot = partition(a, start, end)
        quicksort(a, start, pivot-1)
        quicksort(a, pivot+1, end)


def partition(a, start, end):
    pivot = a[start]
    left = start+1
    right = end

    while left <= right:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if right > left: #swap the elements
            tmp = a[left]
            a[left] = a[right]
            a[right] = tmp

    tmp = a[start]
    a[start] = a[right]
    a[right] = tmp

    return right #return the median index of array


def main():
    my_list = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    print("Start list is: ", my_list)
    quicksort(my_list, 0, len(my_list)-1)
    print("Ordered list is: ", my_list)


if __name__ == "__main__":
    main()
