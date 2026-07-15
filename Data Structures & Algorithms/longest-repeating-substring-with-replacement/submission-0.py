class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1
        
            missmatch = (right - left + 1) - max(count.values())
            
            while missmatch > k:
                count[s[left]] -= 1
                left += 1
                missmatch = right - left - max(count.values())
            
            res = max(res, right - left + 1)

        return res