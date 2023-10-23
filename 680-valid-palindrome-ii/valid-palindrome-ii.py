class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(st, end, first):
            start = st 
            # print(s[start], s[end])
            while(start<=end):
                if s[start] ==s[end]:
                    start +=1 
                    end-=1 
                elif first:
                    #case 01 
                    first = False
                    return check(start+1, end, first) or check(start, end-1, first) 
                else:
                    return False
            return True    
        end = len(s) -1 
        return check(0, end, True)