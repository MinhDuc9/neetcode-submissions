class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        res = float("inf")
        total = 0

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target and left <= right:
                res = min(res, right - left)
                total -= nums[left]
                left += 1
        
        return res if res != float("inf") else 0
