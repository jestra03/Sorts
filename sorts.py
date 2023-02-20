# Sorting Algorithms
# Joshua Estrada
import random
import time
from heap import*


def bogo_sort(arr):
    n = len(arr)
    while True:
        is_sorted = True
        random.shuffle(arr)
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                is_sorted = False
        if is_sorted:
            break
    # Time Complexity: O(n+1)! [Average]
    # Worse case: Infinity
    # Best case: O(n)
    # Bogo Sort || Randomizes array until it is sorted


def bubble_sort(arr):
    comps = 0
    n = len(arr)
    while True:
        is_sorted = True
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                is_sorted = False
            comps += 1
        if is_sorted:
            break
    return comps
    # Average Time Complexity: O(n^2) -> O((n*(n-1))/2)
    # Worse case: O(n^2) -> O((n*(n-1))/2)
    # Best case: O(n^2) -> O((n*(n-1))/2)


"""
    Bubble Sort
    - Switches current element and next element if next element is smaller while iterating through the array O(n^2)
    - repeats swapping process until full array is sorted O(n)
    """


def selection_sort(arr):
    comps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            comps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comps
    # Average Time Complexity: ~O(n^2) -> O((n*(n-1))/2)
    # Worse case: O(n^2) -> O((n*(n-1))/2)
    # Best case: O(n^2) -> O((n*(n-1))/2)


"""
    Selection Sort 
    Finds minimum of array and swaps current element with min element until array is sorted O(n^2)
    """


def insertion_sort(arr):
    comps = 0
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            comps += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return comps
    # Average Time Complexity: O(n^2) -> O((n*(n-1))/4)
    # Worse case: O(n^2) -> O((n*(n-1))/2)
    # Best case: O(n)


"""
    Insertion Sort
    Each element in the unsorted array is inserted into its correct order in the sorted array until sorted O(n^2)
    """


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    # Average Time Complexity: O(n*log(n))
    # Worse case: O(n*log(n))
    # Best case: O(n*log(n))


"""
    Merge Sort
    The array is divided into smaller sub-arrays. The sub-arrays are sorted from the ground up and merged together
    to form the final sorted array. O(n(log(n)))
    """


def hybrid_sort(arr):
    if len(arr) > 10:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        hybrid_sort(left)
        hybrid_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        for i in range(len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
    # Average Time Complexity: O(n*log(n))
    # Worse case: O(n*log(n))
    # Best case: O(n*log(n))


"""
    Hybrid Sort
    This algorithm combines Merge Sort and Insertion Sort to create a sorting algorithm that combines the primary
    advantages of merge sort and insertion sort. 
    
    While Merge Sort is better for sorting large arrays, Insertion Sort performs better on smaller arrays.
    For sub-arrays of length 10 insertion sort handles sorting while merge sort handles the sorting of arrays with
    higher length. This algorithm maintains a time complexity average of O(nlog(n)) while optimizing the sorting 
    process of small arrays.
    """


def main():
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time()
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()
