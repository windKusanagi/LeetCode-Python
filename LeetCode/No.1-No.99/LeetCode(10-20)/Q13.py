class Solution(object):
    def romanToInt(self, s):

        mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1};
        result = mapping[s[0]];
        for i in range( 1, len(s)):
            if mapping[s[i]] > mapping[s[i - 1]]:
                result -= mapping[s[i - 1]]
                result += mapping[s[i]] - mapping[s[i - 1]]
            else:
                result += mapping[s[i]]
        return result

print Solution().romanToInt( "XC");