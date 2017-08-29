# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        stack = []
        self.inOrderT(root , stack)
        if len(stack) == 1:
            return True
        for i in range(1,len(stack)):
            if stack[i] <= stack [i-1]:
                return False
        return True
    def inOrderT (self,  node , stack):
        if node != None:
            self.inOrderT(node.left ,stack)
            stack.append(node.val)
            self.inOrderT(node.right , stack)


root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
print Solution().isValidBST(root)
