# only works for consecutive numbers, i.e. should be able to determine
# index position of each number

# 1) Iterate through the numbers:
# Start from the first number and continue until the end.

# 2) Place each number in its correct place:
# For each number:
# If it's not at its correct index (i.e., number i is not at index i−1), 
# swap it with the number at its correct index.
# Continue this until the number at the iteration is at its correct place and then move on to the next number.

# 3) Terminate:
# The process ends when you've processed all numbers.

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        # If the number is not at its correct index, swap it
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            # Move to the next number
            i += 1
    return nums
