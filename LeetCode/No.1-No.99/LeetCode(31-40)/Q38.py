class Solution(object):
    def countAndSay(self, n):
        result = "1"
        for i in range(1, n):
            result = self.nextNum(result)
        return result

    def nextNum(self, result):
        cas = []
        start = 0
        while start < len(result):
            cur = start + 1
            while cur < len(result) and result[start] == result[cur]:
                cur+=1
            cas.append(str(cur-start))
            cas.append(result[start])
            start = cur
        return "".join(cas)

print Solution().countAndSay(2);

'''
    def nextNum(self, result):
        cas = []
        start = 0
        while start < len(result):
            cur = start + 1
            while cur < len(result) and result[start] == result[cur]:
                cur += 1
            cas.append(str(cur - start))
            cas.append(result[start])
            start = cur
        return "".join(cas)
'''
'''

    def NextNumber(self, result):
        cas = []
        start = 0
        while start < len(result):
            cur = start + 1
            while cur < len(result) and result[cur] == result[cur]:
                cur+=1
            cas.append(str(cur-start))
            cas.append(result[start])
            start = cur
        return "".join(cas)
'''