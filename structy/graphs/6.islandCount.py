# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.





# My iterative solution:

def island_count(grid):
  visited = set()
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if (r,c) not in visited and grid[r][c] == 'L':
        count += 1
        stack = [(r,c)]
        while stack:
          row, col = stack.pop()
          if (row,col) not in visited:
            visited.add((row, col))
            for new_row, new_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
              row_inbounds = 0 <= new_row < len(grid)
              col_inbounds = 0 <= new_col < len(grid[0])
              if row_inbounds and col_inbounds and (new_row, new_col) not in visited and grid[new_row][new_col] == 'L':
                stack.append((new_row, new_col))
  return count



# Same solution but with helper function:
def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] == 'L':
                count += 1
                explore_iteratively(grid, r, c, visited)
    return count

def explore_iteratively(grid, r, c, visited):
    stack = [(r, c)]
    while stack:
        row, col = stack.pop()
        if (row, col) not in visited:
            visited.add((row, col))
            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                row_inbounds = 0 <= new_row < len(grid)
                col_inbounds = 0 <= new_col < len(grid[0])
                if row_inbounds and col_inbounds and (new_row, new_col) not in visited and grid[new_row][new_col] == 'L':
                    stack.append((new_row, new_col))




# Alvin's recursive solution:
def island_count(grid):
  visited = set()
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore(grid, r, c, visited) == True:
        count += 1
  return count

def explore(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return False
  
  if grid[r][c] == 'W':
    return False
  
  pos = (r, c)
  if pos in visited:
    return False
  visited.add(pos)
  
  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)  
  explore(grid, r, c - 1, visited)
  explore(grid, r, c + 1, visited)
  
  return True
