class Solution:
    def mySqrt(self, x: int) -> int:
      upperGuess = x
      lowerGuess = 1

      while lowerGuess <= upperGuess:
        mid = (lowerGuess + upperGuess) // 2

        y = mid ** 2

        if y == x:
          return mid
        elif y > x:
          upperGuess = mid - 1
        else:
          lowerGuess = mid + 1


      return upperGuess