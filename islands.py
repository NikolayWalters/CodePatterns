# problems often revolve around traversing a 2D grid (or matrix) and identifying 
# connected components, often referred to as "islands."

# Problem: Given a 2D grid of 0s (water) and 1s (land), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

# Solution using Depth First Search (DFS):

# 1) Iterate over each cell in the grid.
# 2) If the cell is a 1, increment the island count and start a DFS traversal 
# from that cell to mark all of its connected land cells as visited.

# DFS check if within bounds and not water, i.e.
# if row < 0 or col < 0 or row >= rows or ccol >= cols or grid[r][c] == '0':
#	return

# then check surrounding cells
# Visit all adjacent cells
# dfs(r-1, c)
# dfs(r+1, c)
# dfs(r, c-1)
# dfs(r, c+1)

# 3) To avoid revisiting cells, you can either mark them as 0 after visiting.

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark the cell as visited
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)

    return islands
