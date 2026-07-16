class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = right = 0
        res = 0
        tracking = 0

        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1

            # Tim max cua count. Tim ra chữ cái xuất hiện nhiều nhất
            tracking = max(tracking, count[s[right]])
            right += 1
            
            while right - left - tracking > k:
                count[s[left]] -= 1
                left += 1
        
        res = max(res, right - left)
        
        return res
