def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        unsorted = array[i]

        # a marker to hold the last element of the sorted portion
        marker = i - 1
        
        # loop backwards through the sorted portion
        while marker >= 0:
            counter += 1
            if unsorted < array[marker]:
                swap(array, marker, marker + 1)
            else:
                break
            marker -= 1

    return array, counter