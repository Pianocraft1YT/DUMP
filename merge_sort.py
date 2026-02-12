counter = 0 # to track the number of comparisons

def get_counter():
    return counter

def merge_sort(arr):
    """ Merge Sort, Complexity: O(n log(n)) """
    global counter
    
    # our recursive base case
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    counter += 1 # add to the comparison counter
    # perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # merge each side together
    return merge(left, right, arr.copy())

def merge(left, right, merged):
    """ Merge helper, Complexity: O(n) """

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    # add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    # return result
    return merged

