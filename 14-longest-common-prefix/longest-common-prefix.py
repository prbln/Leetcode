class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        if len(strs) ==1:
            return strs[0]
        for ind in range(1,len(strs)):
            wrd = strs[ind]
            i = 0 
            j = 0 
            while(i<len(wrd) and j<len(lcp)):
                if wrd[i] != lcp[j]:
                    lcp = wrd[:i]
                    break
                i+=1 
                j+=1
            if i == len(wrd) :
                lcp = wrd
        return lcp
                   
        