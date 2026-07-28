class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)

        while right < n:
            nums[left] = nums[right]
            current = nums[left]
            count = 0

            while right < n and nums[left] == nums[right]:
                right += 1
                count += 1

            count = min(count, 2)
            while count:
                nums[left] = current
                left += 1
                count -= 1
            
        return left
