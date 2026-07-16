class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        count = {}
        res = 0
        tracking = 0

        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1

            tracking = max(tracking, count[s[right]])

            while right - left - tracking >= k:
                count[s[left]] -= 1
                left += 1

            right += 1
        
        res = max(res, right - left)

        return res
