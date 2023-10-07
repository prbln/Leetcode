class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) ==0:
            return 0 
        Int = ""
        neg = False
        i = 0 
        if s[0] =="-":
            neg = True
            i+=1
        if s[0] =="+":
            i+=1
        digit = ['1','2','3','4','5','6','7','8','9','0']        
        while(i<len(s) and s[i] in digit):
            Int += s[i]
            i+=1
        if len(Int) ==0:
            return 0 
        if neg:
            if -1*int(Int) < -2147483648:
                return -2147483648
            return -1*int(Int)
        if int(Int) > 2147483647:
            return 2147483647
        return int(Int)