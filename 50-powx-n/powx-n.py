class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            val = power(n//2)
            if n%2 !=0:
                return val*val*x
            return val*val
        if n<0:
            return 1/power(abs(n))
        else:
            return power(n)
