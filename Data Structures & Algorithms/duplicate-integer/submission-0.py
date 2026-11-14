class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      numsSeen = dict()

      for n in nums:
        k = str(n)
        if numsSeen.get(k, None):
          return True

        numsSeen[k] = True

      return False

        