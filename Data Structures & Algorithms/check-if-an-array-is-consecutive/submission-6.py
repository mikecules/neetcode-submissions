class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        lenNums = len(nums)

        return len(set(nums)) == lenNums and ((
            max(nums) - min(nums) + 1) == lenNums)

