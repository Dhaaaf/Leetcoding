# Write a function, string_search, that takes in a grid of letters and a string as arguments. The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. The path can begin at any position, but you cannot reuse a position more than once in the path.

# You can assume that all letters are lowercase and alphabetic.



# My iterative String Search Solutions:
def string_search(grid, s):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == s[0]:
                stack = [(r, c, s[1:], {(r, c)})]
                while stack:
                    curr_r, curr_c, curr_s, visited = stack.pop()
                    if not curr_s:
                        return True
                    for dr, dc, in directions:
                        new_r, new_c = curr_r+dr, curr_c+dc
                        if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == curr_s[0] and (new_r, new_c) not in visited):
                            new_visited = visited.copy()
                            new_visited.add((new_r, new_c))
                            stack.append((new_r, new_c, curr_s[1:], new_visited))
    return False



# Alvin's recursive string search solution:
def string_search(grid, s):
  for r in range(len(grid)):
    for c in range(len(grid[0])):    
      if dfs(grid, r, c, s):
        return True
  return False


def dfs(grid, r, c, s):
  if s == '':
    return True
  
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid)
  if not row_inbounds or not col_inbounds:
    return False
  
  char = grid[r][c]
  if char != s[0]:
    return False
  
  suffix = s[1:]
  
  grid[r][c] = '*'
  
  result = dfs(grid, r + 1, c, suffix) or dfs(grid, r - 1, c, suffix) or dfs(grid, r, c + 1, suffix) or dfs(grid, r, c - 1, suffix)
  grid[r][c] = char
  return result