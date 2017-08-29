class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        stack.append(-1)
        result = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    result = max(result, i - stack[len(stack)-1])
                else:
                    stack.append(i)

        return result

print Solution().longestValidParentheses("(()))())()()()()()")