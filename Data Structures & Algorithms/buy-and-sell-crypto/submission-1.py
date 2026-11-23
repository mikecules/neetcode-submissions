class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = left + 1
        profit = 0

        while right < len(prices):
          buyPrice = prices[left]
          sellPrice = prices[right]
          possible_profit = sellPrice - buyPrice
          profit = max(profit, possible_profit)
          
          if buyPrice > sellPrice:
            left += 1
          else:
            right += 1


        return profit