class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1
        
            freq_char = max(count.values())
            
            while (right - left + 1) - freq_char > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res