class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(selfself, root):
        if not root:
            return []
        result , cur = [], []
        cur.append(root)
        while cur:
            levelRes = []
            nextLevel = []
            for node in cur:
                levelRes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            result.append(levelRes)
            cur = nextLevel
        return result[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = Solution().levelOrderBottom(root)
print result