class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix[i] = total
        
        for i in range(len(nums)):
            leftSum = prefix[i - 1] if i > 0 else 0
            rightSum = prefix[n - 1] - prefix[i]

            if leftSum == rightSum:
                return i
        
        return -1