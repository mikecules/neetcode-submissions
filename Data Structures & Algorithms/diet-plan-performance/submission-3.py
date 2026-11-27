class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        left = 0
        lenCalories = len(calories)
        right = 0 if k == 1 else min(left + 1, lenCalories)
        totalPointAward = 0
        currentTotal = 0

        if right > left:
          currentTotal += calories[left]

        while right < lenCalories:
          currentWindowLength = ((right - left) + 1)

          if currentWindowLength < k:
            currentTotal += calories[right]
            right += 1
            continue

          currentTotal += calories[right]
          pointAward = 0
        
          if currentTotal > upper:
            pointAward = 1
          elif currentTotal < lower:
            pointAward = -1

          totalPointAward += pointAward
          currentTotal -= calories[left]

          left += 1
          right += 1
          
        return totalPointAward