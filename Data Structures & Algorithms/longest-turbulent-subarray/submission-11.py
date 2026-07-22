class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        prev = ""
        res = 1

        while r < len(arr):
            if arr[r] < arr[r - 1] and prev != "<":
                r += 1
                prev = "<"
                res = max(r - l, res)
            elif arr[r] > arr[r - 1] and prev != ">":
                r += 1
                prev = ">"
                res = max(r - l, res)
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""
        
        return res