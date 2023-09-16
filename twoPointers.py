# find pairs, triples, or subarrays that meet a certain criterion.
# especially useful when the array or string is sorted (or can be sorted)

# start with two pointers at different positions (usually the beginning 
# and the end) and move them towards each other or in the same direction, based on some conditions.

# e.g. Problem: Given a sorted array, find a pair of numbers that sum up to a target value.

# 1) Start with two pointers, left at the beginning of the array and right at the end.
# 2) Calculate the sum of the values at the left and right pointers.
# 3) If the sum is equal to the target, we've found a pair.
# 4) If the sum is less than the target, move the left pointer one step to the right.
# 5) If the sum is more than the target, move the right pointer one step to the left.
# 6) Repeat steps 2-5 until the pointers meet.

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
