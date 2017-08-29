# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        cur = []
        cur.append(root)
        level = 0
        while cur:
            nextlevel =[]
            for node in cur:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            cur = nextlevel
            level+=1
        return level

class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
print Solution().maxDepth(root)
print Solution2().maxDepth(root)