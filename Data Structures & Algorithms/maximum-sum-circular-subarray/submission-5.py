class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = currMin = nums[0]
        globalMax = globalMin = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            globalMax = max(currMax, globalMax)
            total += nums[i]
            currMin = min(currMin + nums[i], nums[i])
            globalMin = min(currMin, globalMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
