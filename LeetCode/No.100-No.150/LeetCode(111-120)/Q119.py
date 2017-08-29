class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],[1,1]]
        if numRows <=1:
            return result[numRows]
        for i in range(numRows-1):
            cur = [1]
            for j in range(i+1):
                cur.append(result[i+1][j]+result[i+1][j+1])
            cur+=[1]
            result.append(cur+[])
        return result[numRows]
print Solution().getRow(4)