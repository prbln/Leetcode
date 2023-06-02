class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #idea is to just comapre forst two strings and let this continue
        if len(strs) == 1:
            return strs[0]

        def find_common(s,t):
                ptr1 = 0 
                ptr2 = 0 
                common = ""
                while(ptr1<len(s) and ptr2<len(t)):
                    if s[ptr1] == t[ptr2]:
                        common +=s[ptr1]
                        ptr1+=1
                        ptr2+=1
                    else:
                        break
                return common
        common = find_common(strs[0],strs[1])
        for i in range(2,len(strs)):
            if common =="":
                return ""
            
            common = find_common(common, strs[i])
        return common
        
