class Solution:
    def isHappy(self, n: int) -> bool:
        prevs = set()
        
        while True:
            the_sum = self.sumDigits(n)
            if the_sum == 1:
                return True
            elif the_sum in prevs:
                return False
            else:
                prevs.add(the_sum)


    def sumDigits(self, n: int) -> int:
        tot = 0
        while n > 0:
            digit = n % 10
            tot += digit * digit
            n = n // 10
        
        return tot