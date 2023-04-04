# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Search column for 1-9
        # Search rows for 1-9
        # Search 3x3 blocks for 1-9
        # Use hashmap or a set
        # We loop through
        # Check if element is in hashmap, or set
        # If it exists then false
        # If it doesn't exist we add to map

        row_set = {}
        col_set = {}
        squares_set = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if r not in row_set:
                    row_set[r] = []
                if c not in col_set:
                    col_set[c] = []
                if (r // 3, c // 3) not in squares_set:
                    squares_set[(r // 3, c // 3)] = []
                
                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in squares_set[(r //3, c //3)]:
                    return False

                row_set[r].append(board[r][c])
                col_set[c].append(board[r][c])
                squares_set[(r//3, c//3)].append(board[r][c])
        return True
