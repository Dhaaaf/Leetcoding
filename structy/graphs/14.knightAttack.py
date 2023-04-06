# A knight and a pawn are on a chess board. Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

# Write a function, knight_attack, that takes in 5 arguments:

# n, kr, kc, pr, pc

# n = the length of the chess board
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the row of the pawn
# pc = the column of the pawn
# The function should return a number representing the minimum number of moves required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None


# Mine and Alvin's solution:

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  visited = set()
  visited.add((kr, kc))
  queue = deque([(kr, kc, 0)])

  while queue:
    r, c, moves = queue.popleft()
    position = (r, c)
    
    if (r, c) == (pr, pc):
      return moves
    
    next_moves = knight_moves(n, r, c)
    for move in next_moves:
      row, col = move
      if move not in visited:
        visited.add(move)
        queue.append((row, col, moves +1))
  return None
    
    
    
def knight_moves (n, r, c):
  positions = [(r + 2, c + 1), (r + 2, c - 1),
              (r - 2, c + 1), (r - 2, c - 1),
              (r + 1, c + 2), (r + 1, c - 2),
              (r - 1, c + 2), (r - 1, c -2)]
  
  return [(row, col) for (row, col) in positions if valid_position(n, row, col) ]
      

def valid_position(n, r, c):
  if 0 <= r < n and 0 <= c < n:
    return True
  return False
