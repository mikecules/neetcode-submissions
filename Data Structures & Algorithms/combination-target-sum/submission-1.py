class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        validCombinations: List[List[int]] = []
        len_nums = len(nums)

        def dfs(i: int, currentCombination: List[int], total: int = 0):
            if total == target:
                 validCombinations.append(currentCombination[:])
                 return
            elif total > target or i >= len_nums:
                return
        
            currentCombination.append(nums[i])
            dfs(i, currentCombination, total + nums[i])
            currentCombination.pop()
            dfs(i + 1, currentCombination, total)
        
        dfs(0, [])

        return validCombinations