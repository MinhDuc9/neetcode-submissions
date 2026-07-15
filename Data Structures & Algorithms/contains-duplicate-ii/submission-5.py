class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()
        i = j = 0

        while j < len(nums):
            if nums[j] in windows:
                return True
            
            windows.add(nums[j])

            if j - i >= k:
                windows.remove(nums[i])
                i += 1
            
            j += 1
            
        return False
