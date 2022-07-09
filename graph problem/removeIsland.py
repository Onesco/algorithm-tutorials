grid = [
  ['L', 'L', 'W', 'W'],
  ['W', 'W', 'L', 'W'],
  # ['W', 'W', 'W', 'L'],
  # ['W', 'W', 'L', 'W'],
  # ['L', 'W', 'W', 'L'],

]

def removeIsland(grid):
    count = 0
    is_visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if exploreGrid(grid, r, c, is_visited):
                count += 1
    return count



def exploreGrid(grid, r, c, is_visited):
    print(is_visited)
    col_boundries = 0 <= c & c < len(grid[0])
    row_boundries = 0 <= r & r < len(grid)

    if (not col_boundries or not row_boundries):
        return False

    pos = f"{r},{c}"
    if pos in is_visited:
        return False
    is_visited.add(pos)

    if grid[r][c] =='W':
        return False

    is_left_bound = c == 0
    is_right_bound = c == len(grid[0])
    is_up_Bound = r == 0
    is_down_Bound = r == len(grid)

    right = exploreGrid(grid, r, c+1 , is_visited)
    left = exploreGrid(grid, r, c - 1, is_visited)
    up = exploreGrid(grid, r-1, c, is_visited)
    down = exploreGrid(grid, r + 1, c, is_visited)
    return True

print(removeIsland(grid))