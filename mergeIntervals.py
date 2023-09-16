# Problem Statement:
# You're given a list of intervals, and your task is to merge any overlapping intervals.

# Example:
# Given intervals: [1,3],[2,6],[8,10],[15,18]

# The intervals [1,3] and [2,6] overlap, so they should be merged into [1,6].

# The resulting merged intervals should be: [1,6],[8,10],[15,18]

# Step-by-Step Solution:
# 1) Sort the Intervals:
# Before we can merge, we need to sort the intervals based on their start times. 
# This ensures we're examining the intervals in the order they appear on the number line.

# 2) Initialize Merged List:
# Start with an empty list called merged. Add the first interval from the sorted list to merged.
# merged: [1,3]

# 3) Iterate Over Intervals:
# Now, for each subsequent interval in the sorted list,
#  check if it overlaps with the last interval in the merged list.
# An overlap occurs if the start of the current interval is less than or equal to the end 
# of the last interval in merged.

# 4) Handle Overlap:
# If two intervals overlap, merge them. To merge, update the end of the last interval 
# in merged to be the maximum of its own end and the end of the current interval.

# 5) Handle No Overlap:
# If the current interval doesn't overlap with the last interval in merged, 
# simply add the current interval to merged.

# 6) Continue Iterating:
# Continue this process for all intervals in the sorted list. 
# After processing all intervals, merged will contain the final list of merged intervals.

def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort the intervals based on start times
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    # Step 2: Iterate and merge overlapping intervals
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged_interval = merged[-1]

        if current_interval[0] <= last_merged_interval[1]:
            # Overlapping intervals; merge them
            merged[-1] = [last_merged_interval[0], max(last_merged_interval[1], current_interval[1])]
        else:
            # Non-overlapping intervals; simply append
            merged.append(current_interval)

    return merged
