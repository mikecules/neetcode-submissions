class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        colour_count = [0, 0, 0]


        for j in range(len(nums)):
          colour_count[nums[j]] += 1

        i = 0

        for k in range(len(colour_count)):
          for _n in range(colour_count[k]):
            nums[i] = k
            i += 1
    
        