class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        lenNums = len(nums)

        maxNum = nums[0]
        minNum = nums[0]

        for n in nums:
            maxNum = max(n, maxNum)
            minNum = min(n, minNum)

        return len(set(nums)) == lenNums and ((
            maxNum - minNum + 1) == lenNums)

