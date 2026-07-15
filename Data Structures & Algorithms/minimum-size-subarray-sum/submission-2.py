class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        if res == float('inf'):
            return 0

        return res
