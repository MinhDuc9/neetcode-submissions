class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        maxLeft = [0] * n
        maxCurr = height[0]
        maxLeft[0] = maxCurr
        for i in range(1, n):
            maxLeft[i] = maxCurr
            maxCurr = height[i] if maxCurr < height[i] else maxCurr

        maxRight = [0] * n
        maxRight[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        res = 0
        for i in range(n):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                res += water

        return res

