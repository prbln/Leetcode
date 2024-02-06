class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        for letter in s:
            if not count.get(letter):
                count[letter] = 0 
            count[letter] +=1  
        for letter in t:
            if count.get(letter) == None or count[letter] == 0 :
                return False 
            else:
                count[letter]-=1
        if len(s) == len(t) :
            return True
        return False