# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(selfself, root):
        if not root:
            return []
        result , cur = [], []
        cur.append(root)
        level = 0
        while cur:
            levelRes = []
            nextLevel = []
            for node in cur:
                levelRes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if level %2 ==0:
                result.append(levelRes)
            else:
                result.append(levelRes[::-1])
            level+=1
            cur = nextLevel
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = Solution().zigzagLevelOrder(root)
print result