class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combination(candidates, [] ,target , result)
        return result

    def combination(self, candidates, current, target, result):
        if current:
            curSum = sum(current)
        else:
            curSum = 0
        if curSum > target:
            return
        elif curSum == target:
            result.append(current)
            return
        else:
            i = 0
            while i < len(candidates):
                self.combination(candidates[i+1:], current+[candidates[i]] , target, result)
                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i+=1
                i+=1

print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)