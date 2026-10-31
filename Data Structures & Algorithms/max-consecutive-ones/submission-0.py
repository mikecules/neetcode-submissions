class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones: int = 0
        temp_max_consecutive_ones = 0

        for i in nums:
            if i == 0:
                temp_max_consecutive_ones = 0
            else:
                temp_max_consecutive_ones += 1

            max_consecutive_ones = max(max_consecutive_ones, temp_max_consecutive_ones)
        
        return max_consecutive_ones