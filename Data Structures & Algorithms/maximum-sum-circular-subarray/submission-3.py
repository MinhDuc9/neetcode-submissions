class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        currMax = total = currMin = 0

        for i in nums:
            currMax = max(currMax + i, i)
            globMax = max(globMax, currMax)
            total += i
            currMin = min(currMin + i, i)
            globMin = min(currMin, globMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax