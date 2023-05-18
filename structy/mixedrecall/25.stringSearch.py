



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