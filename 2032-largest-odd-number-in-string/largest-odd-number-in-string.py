class Solution:
    def largestOddNumber(self, num: str) -> str:
        #case 01 given number os odd
        lastDigit = int(num[-1])
        if lastDigit %2 !=0:
            return num 
        #not odd
        i = len(num)-1
        curMaxODD = False
        ans = -1*math.inf
        while(i>=0):
            if int(num[i])%2 != 0:
                return num[:i+1]
            i-=1
        return ""