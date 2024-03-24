class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_frequency_s = dict() 
        letter_frequency_t = dict()
        #Step -1: iterate over string s save count freq of each letter s O(26), O(n)
        for letter in s: 
            if  letter_frequency_s.get(letter, False):
                letter_frequency_s[letter]+=1
            else:
                letter_frequency_s[letter]=1
        #Step -2: iterate over string t save count freq of each letter s O(26), O(n) 
        for letter in t: 
            if  letter_frequency_t.get(letter, False):
                letter_frequency_t[letter]+=1
            else:
                letter_frequency_t[letter]=1
        #match the freq of each letter in both the cases 
        for ascii_value in range(ord('a'), ord('z') + 1):
            alphabet = chr(ascii_value)#O(26)
            if letter_frequency_s.get(alphabet, 0 ) != letter_frequency_t.get(alphabet, 0):
                return False 
        return True

# letter_frequency_s = { a:3, n:1, g:1, r:1, m:1 }
# letter_frequency_t = { a:3, n:1, g:1, r:1, m:1 }
