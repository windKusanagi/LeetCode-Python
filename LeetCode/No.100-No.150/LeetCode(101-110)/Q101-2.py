class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative solution
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p, q = stack.pop(), stack.pop()
            if p == None and q == None:
                continue
            elif p == None or q == None:
                return False
            elif  p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)
        return True

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(2)
root.left.left, root.right.right = TreeNode(3), TreeNode(3)
root.left.right, root.right.left = TreeNode(4), TreeNode(4)
print Solution().isSymmetric(root)
