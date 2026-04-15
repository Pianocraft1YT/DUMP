counter = 0 # to track the number of comparisons

def get_counter():
    return counter

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def bubble_sort(array):
    global counter
    
    n = len(array)-1
    for i in range(0, len(array)):
        for j in range(0, n):
            if array[j] > array[j+1]:
                counter += 1
                swap(array, j+1, j)
        n -= 1
    
    return array, counter

