
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result= []
        k-=1
        curSet = [ i for i in range(1, n+1)]
        factorial = 1
        for i in range(2, n+1):
            factorial*= i
        i = 0
        while i < n:
            factorial/=n-i
            index = k / factorial
            result.append(str(curSet[index]))
            curSet.remove(curSet[index])
            k %= factorial
            i+= 1
        str1= ''.join(result)
        return str1

print Solution().getPermutation(9, 324)
