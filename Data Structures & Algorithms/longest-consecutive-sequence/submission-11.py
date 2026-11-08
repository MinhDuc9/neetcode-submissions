class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        setNums = set(nums)
        numsDict = collections.defaultdict(bool)

        for v in setNums:
            numsDict[v] = True

        for v in setNums:
            if numsDict[v] == False:
                continue
            
            count = 1
            tempUp = v
            tempDown = v
            numsDict[v] = False
            
            while numsDict[tempUp + 1] != False:
                numsDict[tempUp + 1] = False
                tempUp += 1
                count += 1

            while numsDict[tempDown - 1] != False:
                numsDict[tempDown - 1] = False
                tempDown -= 1
                count += 1

            res = max(count, res)
        
        return res