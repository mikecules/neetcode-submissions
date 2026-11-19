class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
          leftChar = s[left].lower()
          rightChar = s[right].lower()
          isLeftCharAlphaNum = leftChar.isalnum()
          isRightCharAlphaNum = rightChar.isalnum()

          if isLeftCharAlphaNum and isRightCharAlphaNum:
            if leftChar != rightChar:
              return False

            left += 1
            right -= 1
          
          if not isLeftCharAlphaNum:
            left += 1

          if not isRightCharAlphaNum:
            right -= 1

        return True
