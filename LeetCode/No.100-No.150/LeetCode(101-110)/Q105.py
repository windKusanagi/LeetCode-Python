# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        return self.buildTbyPI(preorder, 0 , len(preorder) , inorder , 0 , len(inorder))

    def buildTbyPI ( self,preorder ,pres , pree , inorder, ins, ine):
        if pres>= pree:
            return None
        root = TreeNode( preorder[pres])
        cur = inorder[ins:ine+1].index(preorder[pres])
        root.left = self.buildTbyPI( preorder , pres+1 , pres+cur+1 , inorder , ins , ins+cur)
        root.right = self.buildTbyPI( preorder , pres+1+cur , pree , inorder , ins+cur+1 , ine)

        return root

preorder = [1, 2, 3]
inorder = [2, 1, 3]
result = Solution().buildTree(preorder, inorder)
print result.val
print result.left.val
print result.right.val