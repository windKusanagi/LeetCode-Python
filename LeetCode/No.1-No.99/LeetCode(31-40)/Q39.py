class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination( candidates, [] ,target , result)
        return result

    def combination(self, candidates, current, target, result):
        if current:
            curSum = sum(current)
        else:
            curSum = 0
        if curSum == target:
            result.append(current)
            return
        elif curSum > target:
            return
        else:
            for i ,v in enumerate(candidates):
                self.combination(candidates[i:], current+[v] , target, result)
'''

        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination(candidates, target, [], result)
        return result

    def combination(self, candidates, target, current, result):
        CUR = sum(current) if current else 0
        if s > target:
            return
        elif s == target:
            result.append(current)
            return
        else:
            for i, v in enumerate(candidates):
                self.combination(candidates[i:], target, current + [v], result)
'''
print Solution().combinationSum([2, 3, 6, 7], 7)