class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, right = 0, 0
        res = 0

        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            right += 1
            res = max(res, right - left)
        
        return res
