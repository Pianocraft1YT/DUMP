import random
counter = 0 # to track the number of comparisons

def get_counter():
    global counter
    return counter

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def median_of_three(arr, low, high):
    """
    Selects the median of the first, middle, and last elements 
    and places it at arr[high] (as the pivot).
    """
    mid = (low + high) // 2
    # Sort the three elements: arr[low], arr[mid], arr[high]
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Place the pivot (now at arr[mid]) at the 'high' index 
    # for consistent partitioning logic
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]

def partition(array, start, end):
    global counter
    """ quicksort partitioning """
    #pivot = array[end] #Choosing end pivot can cause recursion stack to exceed allow depth (1000)
    #pivot = random.choice(array)  #this still exceeeded recursion depth at array length > 800K
    pivot = median_of_three(array, start, end)
    L = start
    R = end
    while L < R:
        while array[L] < pivot:
            L += 1
            counter += 1
        while array[R] > pivot:
            R -= 1
            counter += 1
        swap(array, L, R)
        # avoid hanging on the same numbers
        if ( array[L] == array[R] ):
            L += 1
    return R

def _quicksort(array, start, end):
    """ Recursive quicksort function """
    global counter
    if start < end:
        counter += 1
        split = partition(array, start, end)
        _quicksort(array, start, split-1)
        _quicksort(array, split+1, end)

def quick_sort(array):
    _quicksort(array, 0, len(array)-1)
    return array, counter
    

