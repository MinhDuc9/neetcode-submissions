from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1

        for i in range(len(nums)):
            prefixSum += nums[i]
            tmp = prefixSum - k
            
            if tmp in sum_map:
                res += sum_map[tmp]
            
            sum_map[prefixSum] += 1
        
        return res
