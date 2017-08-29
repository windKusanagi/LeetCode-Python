'''
class Solution(object):
    def simplifyPath(self, path):
        result = []
        p = list(i for i in path)
        result.append(p[0])
        i = 1
        while i < len(p):
            if p[i] == "." and p[i-1] == ".":
                result=["/"]
            else:
                result.append(p[i])
            i+=1
        i, temp=0 , []
        while i<len(result)-1:
            if result[i] == "/" and result[i+1] == "/":
                temp= result[:i+1]+result[i+2:]
                result = temp
            else:
                i+=1
        if len(result) != 1 and result[-1]=="/":
            result.pop()
        if result[-1] == "." :
            result.pop()
        return "".join(result)
'''
class Solution(object):
    def simplifyPath(self, path):
        parts = path.split("/")
        result = ['']
        for part in parts:
            if part:
                if part not in ('.', '..'):
                    if len(result) == 0:
                        result.append('')
                    result.append(part)
                elif part == '..' and len(result) > 0:
                    result.pop()
        if len(result) < 2:
            return "/"
        else:
            return "/".join(result)

print Solution().simplifyPath("/a///b/../../c/")
print Solution().simplifyPath("/home/")
print Solution().simplifyPath("/../../")
print Solution().simplifyPath("/.")
print Solution().simplifyPath("/...")