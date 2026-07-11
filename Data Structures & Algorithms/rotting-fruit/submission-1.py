class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                        continue
                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1
            res += 1

        return res if fresh == 0 else -1
    
