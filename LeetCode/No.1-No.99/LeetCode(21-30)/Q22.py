class Solution(object):
    def generateParenthesis(self, n):
        result= list()
        result = self.combination ( n, n, "" , result)
        return result

    def combination (self,  left , right , cur , result ):
        if left == 0 and right == 0:
            result.append(cur)
        else:
            if left > 0 :
                self.combination ( left -1 , right , cur+ "(" , result)
            if right > left:
                self.combination ( left , right - 1  , cur+ ")" , result)
        return result

print Solution().generateParenthesis(5)