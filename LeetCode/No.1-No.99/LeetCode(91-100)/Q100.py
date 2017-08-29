# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        flag = True
        flag = self.isSame( p, q)
        return flag

    def isSame(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node2 != None and node1 == None:
            return False
        elif node2 == None and node1 != None:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return self.isSame(node1.left, node2.left) and\
                     self.isSame(node1.right, node2.right)

root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
root2, root2.left, root2.right = TreeNode(5), TreeNode(2), TreeNode(3)
print Solution().isSameTree(root1, root2)