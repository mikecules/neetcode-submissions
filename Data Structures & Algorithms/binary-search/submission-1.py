class Solution:
    def search(self, nums: List[int], target: int) -> int:
      left = 0
      right = len(nums) - 1

      # 7 
      # 7 + 0 // 2 == 3
      # left = 3
      # (3 + 0) // 2 = 1
      # 
      # right = 3
      # (7 - 3) // 2 == 3


      print((3+2)//2)

      while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
          return mid
        elif nums[mid] > target:
          right = mid - 1
        else:
          left = mid + 1


      return -1
        