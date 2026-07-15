class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        currSum = 0
        for i in range(k):
            currSum += arr[i]
        
        if currSum >= threshold * k:
            res += 1

        left = 0
        for right in range(k, len(arr)):
            currSum -= arr[left]
            left += 1
            currSum += arr[right]

            if currSum >= threshold * k:
                res += 1
        
        return res