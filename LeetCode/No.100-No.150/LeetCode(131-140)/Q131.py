class Solution(object):
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s:
            return [[]]
        result = []
        self.partitionRecu(result, [], s, 0)
        return result
    def partitionRecu(self, result, cur, str, pos):
        if pos == len(str):
            result.append(cur + [])
        else:
            for i in range(pos, len(str)):
                if self.isPalindrome(str[pos: i + 1]):
                    self.partitionRecu(result, cur + [str[pos: i + 1]], str, i+1)
    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == "__main__":
    print Solution().partition("aab")