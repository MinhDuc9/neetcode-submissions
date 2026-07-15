class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        prefix = 0

        for i in range(n):
            prefix += nums[i]
            prefixSum[i + 1] = prefix
        
        for i in range(n):
            leftSum = prefixSum[i]
            rightSum = prefixSum[n] - prefixSum[i + 1]
            if leftSum == rightSum:
                return i
        
        return -1