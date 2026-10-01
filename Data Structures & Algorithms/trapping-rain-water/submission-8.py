class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        n = len(height)

        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        maxRight[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        for i in range(n):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp > 0:
                res += temp

        return res
