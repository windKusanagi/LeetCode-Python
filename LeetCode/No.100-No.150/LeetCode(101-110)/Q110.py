#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        flag = self.balanced(root)
        if flag == -1:
            return False
        else :
            return True

    def balanced ( self,  node):
        if not node :
            return 0
        left, right = self.balanced(node.left) , self.balanced(node.right)
        if left == -1:
            return -1
        if right == -1:
            return -1
        if abs(left- right) > 1:
            return -1
        return 1+max(left , right)

root = TreeNode(0)
root.left = TreeNode(1)
result = Solution().isBalanced(root)
print result

root.left.left = TreeNode(2)
result = Solution().isBalanced(root)
print result