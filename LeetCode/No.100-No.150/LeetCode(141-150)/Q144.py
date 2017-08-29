#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        result = []
        self.PreorderT(root,result)
        return result

    def PreorderT(self, node , result):
        if node:
            result.append(node.val)
            self.PreorderT( node.left, result)
            self.PreorderT( node.right,result)
        return

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
print Solution().preorderTraversal(n1)
