class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        memoi_arr = defaultdict(int)
        prefix = 0
        memoi_arr[0] = 1

        for i in range(len(nums)):
            prefix += nums[i]
            tmp = prefix - k
            
            if tmp in memoi_arr:
                res += memoi_arr[tmp]
            
            memoi_arr[prefix] += 1

        return res
