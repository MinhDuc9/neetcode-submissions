class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left = 0
        right = 0
        total = 0

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target and left <= right:
                res = min(res, right - left)
                total -= nums[left]
                left += 1

        return 0 if res == float("inf") else res
