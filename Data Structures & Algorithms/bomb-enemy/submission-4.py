class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        res = 0

        m = len(grid) # Rows
        n = len(grid[0]) # Columns
        
        calGrid = [[0] *  n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "W":
                    calGrid[row][col] = -2
                elif grid[row][col] == "E":
                    calGrid[row][col] = -1
        
        def sweep(cells: List[Tuple[int, int]]) -> None:
            count = 0
            for r, c in cells:
                if calGrid[r][c] == -1:
                    count += 1
                elif calGrid[r][c] == -2:
                    count = 0
                else:
                    calGrid[r][c] += count
        
        for r in range(m):
            cells = [(r, c) for c in range(n)]
            sweep(cells)
            sweep(reversed(cells))

        for c in range(n):
            cells = [(r, c) for r in range(m)]
            sweep(cells)
            sweep(reversed(cells))

        res = -1

        for row in range(m):
            for col in range(n):
                if res < calGrid[row][col]:
                    res = calGrid[row][col]

        if res == -1:
            return 0

        return res
