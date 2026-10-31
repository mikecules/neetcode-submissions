class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        list_len = len(nums)
        if (list_len == 0) or (list_len == 1 and nums[0] == val):
            return 0
        elif list_len == 1 and nums[0] != val:
            return 1


        occurance_count = 0
        PLACEHOLDER_VALUE = -1
        
        for i, num in enumerate(nums):
            if num == val:
                ptr_l = i
                ptr_r = i + 1 
        
                while ptr_r < list_len and nums[ptr_r] == val:
                    ptr_r += 1

                if ptr_r < list_len:
                    nums[ptr_l], nums[ptr_r] = nums[ptr_r], PLACEHOLDER_VALUE

                while ptr_r + 1 < list_len:
                    nums[ptr_r], nums[ptr_r + 1] = nums[ptr_r + 1], nums[ptr_r]
                    ptr_r += 1

                occurance_count += 1            

        return len(nums) - occurance_count