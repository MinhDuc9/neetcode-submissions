class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = 0
        target = k * threshold
        res = 0

        for i in range(len(arr)):
            window += arr[i]

            if i >= k:
                window -= arr[i - k]
            
            if i >= k - 1 and window >= target:
                res += 1

        return res
