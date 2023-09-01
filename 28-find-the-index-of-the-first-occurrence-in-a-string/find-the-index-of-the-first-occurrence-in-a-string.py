class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n =0 
        h = 0 
        while(h<len(haystack)):
            if haystack[h] == needle[n]:
                start = h
                while(n<len(needle) and h<len(haystack) and haystack[h] == needle[n]):
                    h+=1 
                    n+=1 
                # if n<len(needle) and h == len(haystack):
                #     return -1 
                    # print(n,h)
                if n == len(needle):
                    return start 
                else:
                    n = 0 
                    h = start+1
            else:
                h+=1 
        return -1

        