# breaking boundaries
# Write a function, breaking_boundaries, that takes in 5 arguments: a number of rows (m), a number of columns (n), a number of moves (k), a starting row (r), and a starting column (c). Say you were situated in a grid with dimensions m * n. If you had to start at position (r,c), in how many different ways could you move out of bounds if you could take at most k moves. A single move is moving one space up, down, left, or right. During a path you may revisit a position.



def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
  key = (k, r, c)
  if key in memo:
    return memo[key]
  
  row_inbounds = 0 <= r < m
  col_inbounds = 0 <= c < n
  if not row_inbounds or not col_inbounds:
    return 1
  
  if k == 0:
    return 0
  
  count = 0
  
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for delta in deltas:
    d_row, d_col = delta
    count += _breaking_boundaries(m, n, k - 1, r + d_row, c + d_col, memo)
    
  memo[key] = count
  return count
