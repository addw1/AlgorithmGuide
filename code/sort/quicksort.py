# worst : o(n^2)
# average: o(nlgn)
''' Pseudococde
Quicksort(A):
    If len(A) <= 1:
        return
    Pick some x = A[i] at random  Call this the pivot
    PARTITION the rest of A into: 
    L (less than x) and R (greater than x)
    Replace A with  [L, x, R]  (that is, rearrange A in this order)
    Quicksort(L) 
    Quicksort(R)
'''

def quicksort(arr, l, r):
    if l < r:
        mid = partition(arr, l ,r)
        quicksort(arr, l, mid - 1)
        quicksort(arr, mid + 1, r)
def partition(arr, l, r):
    # [l, i] < target
    # [i + 1, r] >= target
    i = l - 1
    target = arr[r]
    for j in range(l, r):
        if arr[j] < target:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i + 1]
    return i + 1

# test
arr = [1, 6, 2, 3, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)
arr = [2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)