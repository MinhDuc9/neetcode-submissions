class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [(grid[0][0], 0, 0)] # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                newR = r + dr
                newC = c + dc

                if (newR < 0 or newC < 0 or
                    newR == N or newC == N or
                    (newR, newC) in visit
                ):
                    continue
                
                visit.add((newR, newC))
                heapq.heappush(minH, (max(t, grid[newR][newC]), newR, newC))

        return -1