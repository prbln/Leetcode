class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = 0 
        fast = 1 
        s =""
        while(fast<len(chars)):
            if chars[prev] == chars[fast]:
                fast+=1
            else:
                if fast - prev == 1: 
                    s +=chars[prev]
                else:
                    s+= chars[prev]
                    s+= str(fast - prev)
                cur = chars[prev]
                while(cur == chars[prev] and prev<len(chars) ):
                    prev+=1 
                fast+=1 
        s+= chars[prev]
        if fast - prev != 1 :
            s+= str(fast - prev)
        count = 0 
        for ind in range(len(s)) :
            chars[ind] = s[ind]
            if s[ind] not in [1,2,3,4,5,6,7,8,9,10]:
                count+=1
        return count
            
                    
        