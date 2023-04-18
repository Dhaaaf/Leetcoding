class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # set to keep track of which positions we've been to
        # set a count as well for our islands
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    count+=1
                    stack = [(r,c)]
                    while stack:
                        row, col = stack.pop()
                        if (row, col) not in visited:
                            visited.add((row, col))
                            neighbors = [(row + 1, col), (row -1, col), (row, col + 1), (row, col -1)]
                            # check neighbors
                            # check if neighbors are valid
                            # Add neighbors to the stack
                            for new_row, new_col in neighbors:
                                row_inbounds = 0 <= new_row < len(grid)
                                col_inbounds = 0 <= new_col < len(grid[0])
                                if row_inbounds and col_inbounds and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                                    stack.append((new_row, new_col))
        return count
