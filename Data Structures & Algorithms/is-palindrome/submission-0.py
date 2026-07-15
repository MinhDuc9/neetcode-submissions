class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s) - 1

        while first < last:
            while first < last and not self.check(s[first]):
                first += 1
            while first < last and not self.check(s[last]):
                last -= 1

            if s[first].lower() != s[last].lower():
                return False

            first += 1
            last -= 1

        return True
    
    def check(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
