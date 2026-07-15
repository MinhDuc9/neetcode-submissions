class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n - 1
        res = 0

        while left < right:
            width = right - left
            height = heights[right] if heights[right] < heights[left] else heights[left]
            total = width * height
            res = max(res, total)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res