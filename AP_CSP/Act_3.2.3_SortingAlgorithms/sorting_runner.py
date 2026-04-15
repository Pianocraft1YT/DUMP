import random
import time
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
import merge_sort
from quick_sort import quick_sort

#Generate array of unique integers, sampled from a range;
#DON'T CHANGE THESE VALUES

def measure_sorting_function(func, array_length=6400):
    #Change the array_length value when you call this function, to process longer arrays

    #Create an array of the specified length, populating it with random numbers 
    array = [random.randint(-array_length, array_length) for _ in range(array_length)]
    
    # print(array) 
    print("\nSort algorithm:", func.__name__)
    print("  Array length:", len(array))

    #Time the execution
    start_time = time.perf_counter()
    result = func(array)
    end_time = time.perf_counter()
    
    if ("merge" in func.__name__):
        # seems like simplest way to get counter from merge_sort, due to recursion
        comparisons = merge_sort.get_counter()
    else:
        comparisons = result[1] #Hacky, but easier to understand
    print(" # comparisons:", comparisons)
    elapsed_time = round(end_time - start_time, 1)
    print(f"  Elapsed time: {elapsed_time} seconds\n")


# Good start value for array_length is 2^13, or 8192 (which you can write as 2**13 in Python)
# Then double it & run again, then again . . . 
# You'll want to COMMENT OUT insertion and bubble sort lines after about 2**16 or so
array_length = 2**13

measure_sorting_function(quick_sort, 16)
measure_sorting_function(quick_sort, 32)
measure_sorting_function(quick_sort, 64)
measure_sorting_function(quick_sort, 128)
measure_sorting_function(quick_sort, 256)
measure_sorting_function(quick_sort, 512)
measure_sorting_function(quick_sort, 1024)
measure_sorting_function(quick_sort, 2048)
measure_sorting_function(quick_sort, 4096)
measure_sorting_function(quick_sort, 8192)
measure_sorting_function(quick_sort, 16384)
measure_sorting_function(quick_sort, 32768)
measure_sorting_function(quick_sort, 65536)
# Merge and Quick sort:  No problem going up to 2^24 or so 
#(though for quick_sort you'll start to hit recursion stack limit; but you could keep going with merge_sort)
# measure_sorting_function(quick_sort, array_length)
# measure_sorting_function(quick_sort, array_length)


