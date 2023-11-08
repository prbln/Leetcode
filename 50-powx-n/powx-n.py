class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if n<0:
            negative = True 
            n = abs(n)
        memo = dict()
        def power(n):
            if n ==0:
                memo[n] = 1 
                return 1
            elif n==1:
                memo[n] = x
                return x 
            elif n == 2:
                memo[n] = x*x
                return x * x  
            if n%2 ==0:
                if memo.get(n, False):
                    return memo[n]
                else:
                    val = power(n//2)
                    memo[n] = val*val
                    print(n,memo[n])
                    return memo[n]
            else:
                if memo.get(n, False):
                    return memo[n]
                else:
                    val1 = power(n//2)
                    val2 = power(n//2 + 1)
                    memo[n] = val1*val2
                    print(n,memo[n])
                    return memo[n]
        
        if negative:
            return 1/power(n)
        else:
            return power(n)
