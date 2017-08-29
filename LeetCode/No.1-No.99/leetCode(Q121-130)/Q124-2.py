# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.__result = -(2**16-1)
        self.PathSum(root)
        return self.__result

    def PathSum ( self , node):
        if not node:
            return 0
        leftSum = self.PathSum(node.left)
        rightSum = self.PathSum(node.right)
        leftSum = max(0,leftSum)
        rightSum = max(0, rightSum)
        self.__result = max(self.__result, node.val+leftSum+rightSum)
        return max(node.val+ max(rightSum, leftSum) , 0)

if __name__ == "__main__":
    T7, T1, T2, T3 , T4, T5, T6 = TreeNode(-1), TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(2), TreeNode(4), TreeNode(-3)
    T1.left, T1.right, T4.left, T4.right = T2, T3, T5,T6
    T7.left, T7.right = T1, T4
    print Solution().maxPathSum(T7)

    T1, T2, T3 = TreeNode(1), TreeNode(2), TreeNode(3)
    T1.left, T1.right= T2, T3
    print Solution().maxPathSum(T1)