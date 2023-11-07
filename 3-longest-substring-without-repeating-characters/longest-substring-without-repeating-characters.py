class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited ={}
        n = len(s)
        st = 0 
        end = 0
        maxiCount = 0 
        curCount = 0 
        while(end<n and st<=end):
            if visited.get(s[end], 0):
                while(end<n and st<=end and visited[s[end]] >0  ):
                    visited[s[st]] -=1
                    st+=1 
                    curCount-=1 
            else:
                while( end<n and st<=end) and visited.get(s[end], 0 ) == 0 :
                    # print(end)
                    visited[s[end]] = visited.get(s[end], 0 ) + 1
                    end+=1 
                    curCount+=1 
            # print(visited)
            maxiCount = max(maxiCount, curCount)
            
        return maxiCount