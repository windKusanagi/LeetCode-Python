class Solution(object):
    def multiply(self, num1, num2):
        if ( len(num1) == 1 and num1[0] == '0') or ( len(num2) == 1 and num2[0] == '0'):
            return '0'
        n1 = num1[::-1]
        n2 = num2[::-1]
        l1 = len(num1)
        l2 = len(num2)
        temp = [0 for __ in range(l1 + l2)]
        for i in range(l1):
            for j in range(l2):
                temp[i + j] += (ord(n1[i])-ord('0')) * (ord(n2[j])-ord('0'))
        carry = 0
        temp2 = []
        for num in temp:
            cur = carry + num
            carry = cur / 10
            temp2.append(str(cur % 10))
        while temp2[len(temp2)-1] == '0':
            temp2.pop();
        result = "".join(temp2)[::-1]
        return result

print Solution().multiply("120", "20000")
print Solution().multiply("0", "3421")