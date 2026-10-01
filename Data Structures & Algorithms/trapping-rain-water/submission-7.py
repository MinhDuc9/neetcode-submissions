class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        n = len(height)

        maxLeft = [0] * n
        maxRight = [0] * n

        maxL = height[0]
        for i in range(n - 1):
            maxL = max(maxL, height[i])
            maxLeft[i + 1] = maxL
        
        maxR = height[n - 1]
        for i in range(n - 1, 1, -1):
            maxR = max(maxR, height[i])
            maxRight[i - 1] = maxR
        
        for i in range(1, n):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp > 0:
                res += temp

        return res
