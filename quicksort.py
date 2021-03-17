import numpy as np

def swap(arr, i, j):
    """
    Swap two elements in an array
    
    Parameters
    ----------
    arr: list
        The array
    i: int
        Index of first element
    j: int
        Index of second element
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quicksort_rec(arr, lo, hi):
    """
    Recursively sort a chunk of the array using
    the quicksort algorithm
    Parameters
    ----------
    arr: list
        The array
    lo: int
        Index of first element in the chunk to be sorted
    hi: int
        Index of last element in the chunk to be sorted
    """
    ## TODO: Fill this in
    pass

def quicksort(arr):
    quicksort_rec(arr, 0, len(arr)-1)

np.random.seed(0)
x = np.random.randint(0, 100, 20).tolist()
quicksort(x)
print(x)