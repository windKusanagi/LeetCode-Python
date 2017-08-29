#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.InorderT(root,result)
        return result

    def InorderT(self, node , result):
        if node:
            self.InorderT( node.left, result)
            result.append(node.val)
            self.InorderT( node.right,result)
        return

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
print Solution().inorderTraversal(n1)
