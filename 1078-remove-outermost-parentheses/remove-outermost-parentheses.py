class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        stack = []
        top = 0
        for i in range(len(s)):
            item = s[i]
            if top == 0:
                stack.append(i)
                top+=1
                continue
            if item ==")":
                x = stack.pop()
                top-=1 
                if top !=0:
                    ans+=item
            else:
                stack.append(i)
                top+=1
                ans+=item
        return ans
        