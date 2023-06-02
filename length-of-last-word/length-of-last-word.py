class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if word=="":
                    continue
                break
            else:
                word+=s[i]
        return len(word)
            