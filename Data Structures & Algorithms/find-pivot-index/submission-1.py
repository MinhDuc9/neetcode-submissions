class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        prefix = [0] * n

        for i in range(n):
            total += nums[i]
            prefix[i] = total
        
        for i in range(n):
            leftSum = prefix[i - 1] if i > 0 else 0
            rightSum = prefix[n - 1] - prefix[i]
            if leftSum == rightSum:
                return i
        
        return -1