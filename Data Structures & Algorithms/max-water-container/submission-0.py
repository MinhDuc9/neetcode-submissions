class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            total_area = width * height

            if total_area > res:
                res = total_area

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return res