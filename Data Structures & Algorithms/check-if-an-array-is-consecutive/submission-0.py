class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        lenNums = len(nums)

        if lenNums == 1:
            return True
            
        minVal = nums[0]
        valsSeen = dict()

        for n in nums:
            minVal = min(minVal, n)
            k = str(n)
            # catch the caseof repeating numbers
            if valsSeen.get(k, None) == 1:
                return False

            valsSeen[k] = 1


        maxVal = minVal + lenNums - 1

        i = minVal

        while i <= maxVal:
            k = str(i)
            if valsSeen.get(k, None) is None:
                return False
            i += 1

        return True

