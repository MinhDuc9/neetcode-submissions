class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)

        while r < n:
            nums[l] = nums[r]
            current = nums[l]
            counts = 0

            while r < n and nums[l] == nums[r]:
                counts += 1
                r += 1

            times = min(counts, 2)

            while times > 0:
                nums[l] = current
                l += 1
                times -= 1

        return l