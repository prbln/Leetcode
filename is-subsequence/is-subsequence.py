class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1 = 0 
        ptr2 = 0 
        while(ptr1<len(s) and ptr2<len(t)):
            # print(ptr1,ptr2, s[ptr1],s[ptr2])
            if s[ptr1] == t[ptr2]:
                ptr1+=1 
                ptr2+=1 
            else:
                ptr2+=1
        if ptr1 ==len(s):
            return True 
        else:
            return False