class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        flag = self.symmetric(root.left, root.right)
        return flag

    def symmetric(self, left, right):
        if  left == None and right==None:
            return True
        elif  left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.symmetric(left.left, right.right) and\
                    self.symmetric(left.right, right.left)

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(2)
root.left.left, root.right.right = TreeNode(3), TreeNode(3)
root.left.right, root.right.left = TreeNode(5), TreeNode(4)
print Solution().isSymmetric(root)