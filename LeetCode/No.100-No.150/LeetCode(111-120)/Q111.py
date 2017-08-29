# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right , sum)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
print Solution().hasPathSum(root, 22)