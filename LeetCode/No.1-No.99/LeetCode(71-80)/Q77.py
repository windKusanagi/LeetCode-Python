from itertools import combinations
class Solution:
    def combine(self, n, k):
        return list(combinations([i for i in range(1, n+1)], k))

'''
class Solution:
    def combine(self, n, k):
        result = []
        self.combineNK(n, result, 0, [], k)
        return result

    def combineNK(self, n, result, start, current, k):
        if k == 0:
            result.append(current+[])
        for i in range(start, n):
            current.append(i + 1)
            self.combineNK(n, result, i + 1, current, k - 1)
            current.pop()
'''
if __name__ == "__main__":
    result = Solution().combine(20, 16)
    print result