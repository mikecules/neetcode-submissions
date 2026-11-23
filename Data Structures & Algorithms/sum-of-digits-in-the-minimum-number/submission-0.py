class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minDigit = min(nums)

        sumDigits = 0

        for c in str(minDigit):
          cInt = int(c)
          sumDigits += cInt

        return 1 if sumDigits % 2 == 0 else 0

