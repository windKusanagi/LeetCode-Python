class Solution(object):
    def longestCommonPrefix(self, strs):
        result="";
        if not strs:
            return result;

        for i in range(len(strs[0])):
            temp= strs[0][i];
            for j in range(len(strs)):
                if len(strs[j]) < i+1:
                    return result;
                if not strs[j][i] == temp:
                    return result;
            result+=temp;

        return strs[0];

print Solution().longestCommonPrefix([""]);
print Solution().longestCommonPrefix(["hello", "heabc", "hell"]);
