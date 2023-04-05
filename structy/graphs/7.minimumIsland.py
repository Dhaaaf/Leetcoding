# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

# My iterative solution:
def minimum_island(grid):
    visited = set()
    min_size = float("inf")
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] == 'L':
                island_size = 0
                stack = [(r, c)]
                while stack:
                    row, col = stack.pop()
                    if (row, col) not in visited:
                        visited.add((row, col))
                        island_size += 1
                        for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                            row_inbounds = 0 <= new_row < len(grid)
                            col_inbounds = 0 <= new_col < len(grid[0])
                            if row_inbounds and col_inbounds and (new_row, new_col) not in visited and grid[new_row][new_col] == "L":
                                stack.append((new_row, new_col))
                min_size = min(min_size, island_size)
    
    return min_size


# Alvin's recursive solution:
def explore_size(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return 0
  
  if grid[r][c] == 'W':
    return 0
  
  pos = (r, c)
  if pos in visited:
    return 0
  visited.add(pos)
  
  size = 1
  size += explore_size(grid, r - 1, c, visited)
  size += explore_size(grid, r + 1, c, visited)  
  size += explore_size(grid, r, c - 1, visited)
  size += explore_size(grid, r, c + 1, visited)
  return size
