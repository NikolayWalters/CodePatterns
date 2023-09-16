# This is a variation of the two-pointers technique where the 
# pointers represent the start and the end of a "window" that slides over 
# the array or string. This is particularly useful when you need to 
# find a subarray or substring that meets certain conditions.

# e.g. Problem: Given an array of positive numbers and a positive number 'S', 
# find the length of the smallest contiguous subarray whose sum is greater 
# than or equal to 'S'. Return 0 if no such subarray exists.

# 1) Start with two pointers, start and end, both at position 0.
# 2) Expand the end pointer to the right until the sum of the window is greater than or equal to 'S'.
# 3) Now, shrink the window from the start side to see if we can find a 
# smaller subarray with a sum greater than or equal to 'S'.
# 4) Continue this process until end reaches the end of the array.

def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = float('inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element
        # Shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == float('inf'):
        return 0
    return min_length
