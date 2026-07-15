class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = k - 1
        currTotal = 0
        res = 0

        for i in range(k):
            currTotal += arr[i]
        
        if currTotal / k >= threshold:
            res += 1
        
        for i in range(k, len(arr)):
            currTotal -= arr[left]
            
            left += 1
            right += 1

            currTotal += arr[right]

            if currTotal / k >= threshold:
                res += 1
        
        return res
