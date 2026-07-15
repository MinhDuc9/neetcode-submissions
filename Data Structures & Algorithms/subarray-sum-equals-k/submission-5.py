class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        memoi_arr = defaultdict(int)
        memoi_arr[0] = 1
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            tmp = prefix_sum - k

            if tmp in memoi_arr:
                res += memoi_arr[tmp]
            
            memoi_arr[prefix_sum] += 1
        
        return res