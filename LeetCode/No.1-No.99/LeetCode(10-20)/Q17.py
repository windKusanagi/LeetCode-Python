class Solution(object):

    def letterCombinations(self, digits):

        if not digits:
            return []

        digitletters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        self.combine (digits, "", result , digitletters)
        return result

    def combine(self, digits, current, result, digitletters):
        if not digits:
            result.append(current)
            return

        for c in digitletters[int(digits[0])]:
            self.combine(digits[1:], current + c, result, digitletters)


if __name__ == "__main__":
    print Solution().letterCombinations("23");