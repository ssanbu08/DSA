# Implementation of Bubble Sort algorithm.


def swap(items, index1, index2):
    """Exchange the elements betweeen the given indexes."""
    temp = items[index1]
    items[index1] = items[index2]
    items[index2] = temp


def bubble_sort(arr):
    """Sorts the elements in ascending order."""
    n = len(arr)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr


def num_exchanges(arr):
    """Counts the number of exchanges required for each
    element to reach its final position in the sorted
    array.
    """
    n = len(arr)
    swap_count = [0]*n
    # At the end of each iteration of this loop
    # places the larger elements towards the end.
    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                swap_count[n-1-i] += 1
    return swap_count


def main():
    """Main."""
    arr = [9, 7, 6, 4, 3, 2]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)

    arr = [15, 14, 16, 9, 23, 2]
    swap_count = num_exchanges(arr)
    print(swap_count)


if __name__ == '__main__':
    main()        