class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1:
            return [[1]]
        if numRows ==2:
            return [[1], [1,1]]

        ans = [[1], [1,1], [1,2,1]]
        lastRow = [1,2,1]
        for i in range(3,numRows):
            # print(lastRow)
            nxtRow = [1]
            for j in range(len(lastRow)-1):
                nxtRow.append(lastRow[j] + lastRow[j+1] )
                # print(j)
            nxtRow.append(1)
            lastRow = nxtRow
            ans.append(nxtRow)
        return ans


            






