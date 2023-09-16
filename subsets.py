# This pattern involves generating all subsets of a set.

# A recursive approach involves making a decision for each element: either include it in the current subset 
# or exclude it. We start with an empty subset and explore both possibilities for each element in the input set.

def subsets(nums):
    def backtrack(start=0, current=[]):
        if start == len(nums):
            output.append(current[:])
            return
        # Exclude the current element
        backtrack(start+1, current)
        # Include the current element
        backtrack(start+1, current + [nums[start]])

    output = []
    backtrack()
    return output