class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        curr = 0

        for i in range(n):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        
        return res