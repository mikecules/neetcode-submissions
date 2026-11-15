class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLookup = dict()

        for i, n in enumerate(nums):
          numsLookup[str(n)] = i

        for i, n in enumerate(nums):
          indexOfVal = numsLookup.get(str(target - n), None)

          if not indexOfVal is None and i != indexOfVal:
            return [i, indexOfVal]

        return []