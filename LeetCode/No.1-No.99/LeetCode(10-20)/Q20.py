class Solution(object):
    def isValid(self, s):
        if len(s)%2 == 1:
            return False
        left = ( "(",  "{", "[" )
        right = ( ")",  "}", "]" )
        stack = list()
        for p in s:
            if p in left:
                stack.append(p)
            else:
                if len( stack ) == 0:
                    return False
                elif not left.index(stack.pop()) == right.index(p):
                    return False
        return True if len(stack) == 0 else False

print Solution().isValid("()[]{}")
print Solution().isValid("()[{]}")
