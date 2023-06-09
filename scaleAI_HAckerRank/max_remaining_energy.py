# Matrix traversal start with 100 energy and on any cell on the first row. Each move loses energy value of the cell. Can only move I+1, and j, j-1, j+1,

# It is ok to have negative energy, but er can only move to adjacent nodes and have to start on the first row now the last one



def max_remaining_energy(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    dp[0] = [100 - x for x in matrix[0]]

    for i in range(1, num_rows):
        for j in range(num_cols):
            max_prev_energy = float('-inf')
            for dj in [-1, 0, 1]:
                if 0 <= j + dj < num_cols:
                    max_prev_energy = max(max_prev_energy, dp[i-1][j+dj])
            dp[i][j] = max_prev_energy - matrix[i][j]
    
    return max(dp[-1])