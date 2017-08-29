class Solution(object):
    def addBinary(self, a, b):
        if a[0] == '0' and  b[0] == '0':
            return '0'
        if len(a) > len(b):
            a,b = b,a
        l1, l2 = [int(i) for i in a] , [int(i) for i in b]
        l1, l2 = l1[::-1] , l2[::-1]
        length1,length2 = len(l1), len(l2)
        result = [ 0 for __ in range(length2+1)]
        carry = 0v
        for i in range(length1):
            result[i] = l1[i] + l2[i] + carry
            if result[i] >= 2:
                result[i] = result[i] %2
                carry = 1
            else:
                carry = 0
        for i in range(length1 , len(result)-1):
            result[i] = l2[i]
        i = length1
        while carry == 1:
            result[i]+=carry
            if result[i] == 2:
                result[i] = 0
                i+=1
            else:
                carry = 0
        while result[-1] == 0:
            result.pop()
        result1 = [str(i) for i in result]
        return ''.join(result1[::-1])
print Solution().addBinary("1111000", "111")