# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(selfself, root):
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
        return result

'''
class Solution(object):
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        curr_level = [root]
        while curr_level:
            level_result = []
            next_level = []
            for temp in curr_level:
                level_result.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            result.append(level_result)
            curr_level = next_level
        return result
'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = Solution().levelOrder(root)
print result