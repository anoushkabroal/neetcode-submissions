class Solution:
    def isHappy(self, n: int) -> bool:
        prevs = set()
        
        while n not in prevs:
            prevs.add(n)
            n = self.sumDigits(n)
            if n == 1:
                return True
        return False


    def sumDigits(self, n: int) -> int:
        tot = 0
        while n > 0:
            digit = n % 10
            tot += digit * digit
            n = n // 10
        
        return tot