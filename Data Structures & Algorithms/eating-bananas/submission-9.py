class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        num_piles = len(piles)

        # O(n)
        eat_banana_rate = max(piles)
        if num_piles == h:
          return eat_banana_rate

        # O(n)
        lower_rate = 1
        upper_rate = eat_banana_rate

        while lower_rate <= upper_rate:
          mid_rate = (lower_rate + upper_rate) // 2
          total_time_hours = 0

          for p in piles:
            total_time_hours += math.ceil(float(p) / mid_rate)
         
          if total_time_hours <= h:
            eat_banana_rate = mid_rate
            upper_rate = mid_rate - 1
          else:
            lower_rate = mid_rate + 1


        return eat_banana_rate
