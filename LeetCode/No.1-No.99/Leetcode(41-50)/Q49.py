class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return []
        dict = {}
        result = []
        for i in range (len(strs)):
            if ''.join(sorted(strs[i])) not in dict:
                dict[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                dict[''.join(sorted(strs[i]))].append(strs[i])

        for i in dict.values():
            result += [i]
        return result

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
