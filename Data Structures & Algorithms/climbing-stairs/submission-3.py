_cached_calc = dict()
class Solution:
    def climbStairs(self, n: int) -> int:
        cached_calc1 = _cached_calc.get(str(n))
        
        if cached_calc1:
          return cached_calc1
        
        if n <= 0:
          return 0
        elif n == 1:
          return 1
        elif n == 2:
          return 2

        a = self.climbStairs(n - 1)
        b = self.climbStairs(n - 2)
        _cached_calc[str(n - 1)] = a
        _cached_calc[str(n - 2)] = b
      

        return a + b