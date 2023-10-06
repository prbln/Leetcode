class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        integerFrom = []
        ans = 0 
        for number in s:
            integerFrom.append(roman_numerals[number])
        for i in range(len(integerFrom)-1):
            if integerFrom[i+1]>integerFrom[i]:
                ans+= -1*integerFrom[i]
            else:
                ans+=integerFrom[i]
        return ans+integerFrom[-1]


            