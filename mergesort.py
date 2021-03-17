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

def merge(x, y, i1, mid, i2):
    """
    Perform a merge of two contiguous sorted sub-chunks of
    the array x, using y as a staging area

    Parameters
    ----------
    x: list
        The main array
    y: list
        The array to copy into as the two chunks are being merged
    i1: int
        Left of first chunk
    mid: int
        Right of first chunk
    i2: int
        End of second chunk
    """
    ## TODO: Fill this in
    pass


def mergesort_rec(x, y, i1, i2):
    """
    A recursive call to sort a subset of the array

    Parameters
    ----------
    x: list
        Array to sort
    y: list
        A temporary array / staging area to store intermediate results
    i1: int
        First index of chunk to sort, inclusive
    i2: int
        Second index of chunk to sort, inclusive (i2 >= i1)
    """
    if (i1 == i2):
        # Base case: A single number
        return
    elif (i2 - i1 == 1):
        # Base case: A pair of numbers right next to each other
        if (x[i2] < x[i1]):
            swap(x, i1, i2)
    else:
        # More than two; need to "divide and conquer"
        mid = (i1 + i2)//2
        mergesort_rec(x, y, i1, mid)
        mergesort_rec(x, y, mid+1, i2)
        merge(x, y, i1, mid, i2)


def mergesort(x):
    """
    An entry point for merge sort on the entire array

    Parameters
    ----------
    x: list
        Array to sort
    """
    y = [0]*len(x)
    mergesort_rec(x, y, 0, len(x)-1)

np.random.seed(0)
x = np.random.randint(0, 100, 20).tolist()
mergesort(x)
print(x)