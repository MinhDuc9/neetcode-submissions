class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        tmp = 0

        while l < r:
            tmp = numbers[l] + numbers[r]

            if tmp > target:
                r -= 1
            elif tmp < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return None
        