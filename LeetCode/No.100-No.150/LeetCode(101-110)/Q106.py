class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        return self._buildTree(0, len(inorder) , postorder , inorder)

    def _buildTree(self, start, end , postorder , inorder):
        if start < end:
            root = TreeNode(postorder.pop() )
            index = inorder.index(root.val)
            root.right = self._buildTree(index + 1, end , postorder ,inorder)
            root.left = self._buildTree(start, index , postorder ,inorder)
            return root

inorder = [2, 1, 3]
postorder = [2, 3, 1]
result = Solution().buildTree(inorder, postorder)
print result.val
print result.left.val
print result.right.val