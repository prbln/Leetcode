class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {
            "I" :1, 
            "IV": 4,
            "V" : 5,
            "IX" : 9, 
            "X" : 10, 
            "L" : 50,
            "XL" : 40,
            "C": 100, 
            "XC": 90, 
            "D": 500, 
            "CD": 400,
            "M" : 1000,
            "CM" : 900
        }
        val = 0 
        i = 0 
        n = len(s)
        while(i<n):
            if i != n-1:
                if romanNumerals.get(s[i]+s[i+1],0):
                    val += romanNumerals[s[i]+s[i+1]]
                    i+=2
                    continue
            val += romanNumerals[s[i]]
            i+=1
        return val

            
