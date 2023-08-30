class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ind = 0 
        top = 0
        for ele in intervals:
            if len(ans) ==0:
                ans.append(ele)
                top = ele
            else:
                # print(top,ele)
                if top[1]>=ele[0]:
                    ans.pop()
                    newInterval = [top[0],max(ele[1], top[1])]
                    ans.append(newInterval )
                    top = newInterval 
                else:
                    ans.append(ele)
                    top = ele
        return ans