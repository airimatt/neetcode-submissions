class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited = set()
                    q = deque()
                    q.append((r, c, 0))

                    while q:
                        r, c, prevVal = q.popleft()
                        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                            continue
                        grid[r][c] = min(grid[r][c], 1 + prevVal)
                        # record cell
                        visited.add((r, c))
                        # add neighbors
                        q.append((r + 1, c, grid[r][c]))
                        q.append((r - 1, c, grid[r][c]))
                        q.append((r, c + 1, grid[r][c]))
                        q.append((r, c - 1, grid[r][c]))


            

