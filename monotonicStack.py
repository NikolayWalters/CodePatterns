# A monotonic stack is a stack that maintains a monotonic (either increasing or decreasing) 
# order of elements. It's a useful data structure for solving problems where you need to 
# track elements that are strictly larger or smaller than the current one.

# Example: Next Greater Element
# Given an array, for each element, find the next element in the array that's larger. 
# If there's no such element, output -1 for that element.

def next_greater_element(nums):
    res = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop() # returns the last element of stack and removes it from stack
            res[idx] = nums[i]
        stack.append(i)

    return res


nums = [4, 5, 2, 10, 8]
print(next_greater_element(nums))  # Outputs: [5, 10, 10, -1, -1]
