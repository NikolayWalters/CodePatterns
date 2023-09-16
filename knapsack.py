# You are given weights and values of n items, and you have a knapsack of capacity 
# W. You need to determine the maximum value the knapsack can hold, where you can 
# pick any combination of the items, but you can pick each item only once and the total 
# weight must not exceed the knapsack's capacity.

def knapsack(values, weights, W):
    n = len(values)
    # Initialize a table with dimensions (n+1) x (W+1) to all zeros
    dp = [[0 for x in range(W + 1)] for y in range(n + 1)]

    # Build the dp table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]
