#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        self.PostorderT(root,result)
        return result

    def PostorderT(self, node , result):
        if node:
            self.PostorderT( node.left, result)
            self.PostorderT( node.right,result)
            result.append(node.val)
        return

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
print Solution().postorderTraversal(n1)
