class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        unmatched = 0 
        for bracket in s:
            if bracket == "(":
                stack.append("(")
            elif len(stack) ==0:
                unmatched +=1 
            else:
                stack.pop()
        return unmatched + len(stack)