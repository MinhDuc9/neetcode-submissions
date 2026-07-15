class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = nums[0]
        globMin = nums[0]
        currMax = 0
        currMin = 0
        total = 0

        for i in nums:
            currMax = max(currMax + i, i)
            globMax = max(globMax, currMax)
            total += i
            currMin = min(currMin + i, i)
            globMin = min(globMin, currMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax