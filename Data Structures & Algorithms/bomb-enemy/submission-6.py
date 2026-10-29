class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid) # Row
        n = len(grid[0]) # Column

        calGrid = [[0] * n for _ in range(m)]

        def sweep(cell: List[Tuple[int, int]]) -> None:
            count = 0

            for row, col in cell:
                if grid[row][col] == "E":
                    count += 1
                elif grid[row][col] == "W":
                    count = 0
                else:
                    calGrid[row][col] += count

        for row in range(m):
            cell = [(row, col) for col in range(n)]
            sweep(cell)
            sweep(reversed(cell))
        
        for col in range(n):
            cell = [(row, col) for row in range(m)]
            sweep(cell)
            sweep(reversed(cell))
        
        res = 0
        for row in range(m):
            for col in range(n):
                if res < calGrid[row][col]:
                    res = calGrid[row][col]
        
        return res
