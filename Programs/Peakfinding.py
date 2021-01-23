"""
    Given an integer array nums, find a peak element, and return its index.
    If the array contains multiple peaks, return the index to any of the peaks.
"""

"""Sol: Interative Binary Search approach"""


def findpeakelement(arr):
    n = len(arr)  # length of the array
    # base case for the peak element, if length of the array is 1 or 2.
    if n == 1:
        return 0
    if n == 2:  # returning the index of the larget element in the 2 elements of arr
        return arr.index(max(arr))
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2  # '//2' taking a floor value to avoid the mid value as float
        if mid in range(1, n - 1):  # taking the mid value in between zero and second last element
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] < arr[mid - 1]:
                # set the end element to mid - 1 and it will be the half array from o to mid-1 size
                end = mid - 1
            else:
                start = mid
        if mid == 0:  # edge case: if peak element is at zero index
            if arr[mid] > arr[mid + 1]:
                return 0
            else:
                return 1
        if mid == n - 1:  # edge case: if peak element at last index
            if arr[mid] > arr[mid - 1]:
                return n - 1
            else:
                return n - 2


arr = [10, 15, 20, 19]

print(findpeakelement(arr))
