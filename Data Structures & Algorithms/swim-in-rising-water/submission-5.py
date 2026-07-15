class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dist = [[float('inf')] * N for _ in range(N)]
        dist[0][0] = grid[0][0]
        minH = [(grid[0][0], 0, 0)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while minH:
            t, r, c = heapq.heappop(minH)

            # Water level is different so can't swim
            if t != dist[r][c]:
                continue

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    nt = max(t, grid[nr][nc])
                    if nt < dist[nr][nc]:
                        dist[nr][nc] = nt
                        heapq.heappush(minH, (nt, nr, nc))
        
        return -1