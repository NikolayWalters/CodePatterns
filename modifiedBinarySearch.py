# involves adapting the classic binary search algorithm 

# Classic Binary Search:
# In the classic binary search, you're given a sorted list and a target. 
# The algorithm checks the middle of the list and based on the comparison with 
# the target, it discards half of the list, continuing the search in the remaining half.

# Examples of Modified Binary Search Problems:
# Search in a Rotated Sorted Array: The array is sorted but rotated, and you need to find an element in it.
# Find Peak Element: Given an array, find an index where the value is greater than its neighbors.
# Find First or Last Occurrence of an Element: In a sorted array that contains duplicates, find the first or last occurrence of a target element.
# Find Smallest Letter Greater Than Target: Given a list of sorted characters and a target letter, find the smallest character that is larger than the target.
# Find the Start and End Position of a Subarray with a Given Sum: You need to find a subarray that sums to a particular value.

# taking Find Peak Element as an example
# Input: nums = [1, 3, 20, 4, 1, 0]
# Output: 2 (because nums[2] = 20 is a peak element)

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:  # Move to the right half if the next element is greater
            left = mid + 1
        else:  # Otherwise, move to the left half
            right = mid
    return left  # or right; both will point to the peak element
