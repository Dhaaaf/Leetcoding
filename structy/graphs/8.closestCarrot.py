# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.



# My iterative solution:
from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  queue = deque([((starting_row, starting_col), 0)])
  
  while queue:
    ((r, c), distance) = queue.popleft()
    if grid[r][c] == "C":
      return distance
    if (r,c) not in visited:
      visited.add((r,c))
      for new_row, new_col in [(r +1, c), (r -1, c), (r, c+1), (r, c -1)]:
        valid_row = 0 <= new_row < len(grid)
        valid_col = 0 <= new_col < len(grid[0])
        if valid_row and valid_col and (new_row, new_col) not in visited and grid[new_row][new_col] != "X":
          queue.append(((new_row, new_col), distance +1))
  return -1


# Alvin's solution:

from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set([ (starting_row, starting_col) ])
  queue = deque([ (starting_row, starting_col, 0) ])
  while queue:
    row, col, distance = queue.popleft()
    
    if grid[row][col] == 'C':
      return distance
    
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col      
      pos = (neighbor_row, neighbor_col)
      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <= neighbor_col < len(grid[0])
      if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
        visited.add(pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
        
  return -1
