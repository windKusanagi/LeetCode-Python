# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        stack = []
        dummy = root
        while dummy:
            if dummy.left:
                if dummy.right:
                    stack.append(dummy.right)
                    dummy.right = dummy.left
                    dummy.left = None
            if not dummy.right and stack:
                dummy.right = stack.pop()
            dummy = dummy.right
root = TreeNode(1)
root.left = TreeNode(2)
'''
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)'''
Solution().flatten(root)
print root.val
print root.right.val
'''
print root.right.right.val
print root.right.right.right.val
print root.right.right.right.right.val
print root.right.right.right.right.right.val'''