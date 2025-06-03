"""
---------------------------------------------------------------
Author: Laura Estremera
Date: October 2024
Class: 380 - Design and Analysis of Algorithms
Professor: Dr. Devon Simmonds
Program: QuickSelect Comparison - Lomuto vs. Hoare Partition
---------------------------------------------------------------

Description:
This Python program implements the Quickselect algorithm to find the
k-th smallest element in a list using two different partitioning schemes:
1. Lomuto's Partition
2. Hoare's Partition

The program compares the performance of these two partitioning methods
using two metrics:
(a) The number of swaps made during partitioning
(b) The overall runtime of Quickselect

The program is tested on four lists of increasing sizes:
1. Small List (~20 items)
2. Medium List (~1,000 items)
3. Large List (~10,000 items)
4. Very Large List (~100,000 items)

For each list, k is set to the median item. The results include the
median value, the number of swaps, and the time taken for each partitioning
scheme.

Assumptions:
- The input lists are randomly generated with integer values.
- The list size and k value are hardcoded for each test case.
---------------------------------------------------------------
"""

import random
import time


# Lomuto partition scheme
def lomuto_partition(arr, low, high):
    pivot = arr[low]  # Select pivot as the first element in the array
    i = low + 1  # Initialize the index to place elements smaller than pivot
    swaps = 0  # Initialize swap counter

    for j in range(low + 1, high + 1):  # Traverse through the rest of the array
        if arr[j] < pivot:  # If element is smaller than the pivot
            arr[i], arr[j] = arr[j], arr[i]  # Swap element at i with element at j
            swaps += 1  # Increment swap count
            i += 1  # Increment i to prepare for the next smaller element

    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Place pivot in its correct position
    swaps += 1  # Count the final swap of placing the pivot
    return i - 1, swaps  # Return pivot index and total number of swaps


# Hoare partition scheme
def hoare_partition(arr, low, high):
    pivot = arr[low]  # Select pivot as the first element in the array
    i = low - 1  # Initialize left pointer
    j = high + 1  # Initialize right pointer
    swaps = 0  # Initialize swap counter

    while True:
        i += 1  # Move i to the right until an element >= pivot is found
        while arr[i] < pivot:
            i += 1
        j -= 1  # Move j to the left until an element <= pivot is found
        while arr[j] > pivot:
            j -= 1
        if i >= j:  # If pointers cross, partitioning is done
            return j, swaps  # Return the index of j and total swaps
        arr[i], arr[j] = arr[j], arr[i]  # Swap elements at i and j
        swaps += 1  # Count the swap


# Quickselect algorithm to find the k-th smallest element
def quickselect(arr, low, high, k, partition_type):
    # Initialize pivot_index and swaps to handle cases where they might not be set
    pivot_index = -1
    swaps = 0

    if low == high:  # Base case: only one element left
        return arr[low], 0  # Return the element and no swaps

    # Choose the partitioning scheme based on user input
    if partition_type == 'lomuto':  # If using Lomuto partition
        pivot_index, swaps = lomuto_partition(arr, low, high)
    elif partition_type == 'hoare':  # If using Hoare partition
        pivot_index, swaps = hoare_partition(arr, low, high)

    # Determine if the pivot index matches k
    if k == pivot_index:  # If pivot is the k-th element, return it
        return arr[k], swaps
    elif k < pivot_index:  # If k is in the left partition
        result, sub_swaps = quickselect(arr, low, pivot_index - 1, k, partition_type)
        return result, swaps + sub_swaps  # Accumulate the swaps
    else:  # If k is in the right partition
        result, sub_swaps = quickselect(arr, pivot_index + 1, high, k, partition_type)
        return result, swaps + sub_swaps  # Accumulate the swaps


# Measure performance: the median, number of swaps, and time taken for a partition
# Measure performance: the median, number of swaps, and time taken for a partition
def measure_performance(arr, partition_type):
    k = len(arr) // 2  # k is the median (middle index)
    arr_copy = arr[:]  # Create a copy of the array to avoid modifying the original
    # Using time.perf_counter instead of time.time because time.time is based on the system clock, which can be adjusted
    # by the user or the system admin which means that it could potentially go backwards if the system time is changed.
    # Although time.time() is suitable for general timekeeping tasks that don't require precision, time.perf_counter()
    # is preferred for measuring short durations. The reference point of te returned value is undefined, so only the
    # difference between the two calls is meaningful. Additionally, it is based on a monotonic clock, meaning it ALWAYS
    # increments and never goes backwards.
    start_time = time.perf_counter()  # Start the timer with perf_counter

    result, swaps = quickselect(arr_copy, 0, len(arr_copy) - 1, k, partition_type)
    elapsed_time = time.perf_counter() - start_time  # Calculate the time taken using perf_counter

    return result, swaps, elapsed_time  # Return median, swaps, and time


# Assumptions:
# - The lists are generated with random integers.
# - The median is chosen as k (the middle index).
# - The performance of both partition schemes will be tested on various list sizes.
# Main execution
if __name__ == "__main__":
    # Test cases with different list sizes
    test_lists = {
        'Small': [random.randint(1, 100) for _ in range(20)],  # Small list of 20 elements
        'Medium': [random.randint(1, 1000) for _ in range(1000)],  # Medium list of 1000 elements
        'Large': [random.randint(1, 10000) for _ in range(10000)],  # Large list of 10,000 elements
        'Very Large': [random.randint(1, 100000) for _ in range(100000)],  # Very large list of 100,000 elements
    }

    # Loop through each test list
    for name, test_list in test_lists.items():
        print(f"\nTesting on {name} List:")

        # Lomuto's Partition
        median_lomuto, swaps_lomuto, time_lomuto = measure_performance(test_list, 'lomuto')
        print(f"Lomuto: Median = {median_lomuto}, Swaps = {swaps_lomuto}, Time = {time_lomuto:.6f} seconds")

        # Hoare's Partition
        median_hoare, swaps_hoare, time_hoare = measure_performance(test_list, 'hoare')
        print(f"Hoare: Median = {median_hoare}, Swaps = {swaps_hoare}, Time = {time_hoare:.6f} seconds")
