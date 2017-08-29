class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],[1,1]]
        if numRows <=2:
            return result[:numRows]
        for i in range(numRows-2):
            cur = [1]
            for j in range(i+1):
                cur.append(result[i+1][j]+result[i+1][j+1])
            cur+=[1]
            result.append(cur+[])
        return result
print Solution().generate(6)