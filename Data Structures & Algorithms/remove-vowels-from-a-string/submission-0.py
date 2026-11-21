class Solution:
    def removeVowels(self, s: str) -> str:
      newStrList = []

      for i, char in enumerate(s.lower()):
        if char in ['a', 'e', 'i', 'o', 'u']:
          continue

        newStrList.append(s[i])

      return ''.join(newStrList)

