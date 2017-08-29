class Solution(object):
    def myPow(self, x, n):
        flag = 1 if n >= 0 else -1
        n = abs(n)
        result = 1;
        result = self.exp(x,n)
        if flag < 0:
            result = 1.0 / result
        return result
    def exp(self, x,n):
        if(n==1):
            return x;
        if(n==0):
            return 1;
        if( n%2 == 0 ):
            return self.exp(x*x, n/2)
        return x*self.exp(x*x , n/2);

print Solution().myPow(2, -1)