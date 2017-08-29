# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        result = []
        self.dfsPathSum( root , sum , [] ,  result)
        return result

    def dfsPathSum(self , node ,lsum ,cur ,result):
        if not node:
            return
        cur.append(node.val)
        if not node.left and not node.right and sum (cur)== lsum  :
            result.append(cur+ [])
        if node.left:
            self.dfsPathSum(node.left, lsum, cur,result )
        if node.right:
            self.dfsPathSum(node.right, lsum, cur, result )
        cur.pop()

    def dfsPathSum2(self, root, sum, curr, result):
        if not root:
            return
        sum -= root.val
        if sum == 0 and root.left is None and root.right is None:
            result.append(curr + [root.val])
        if root.left:
            self.dfsPathSum2(root.left, sum, curr + [root.val], result)
        if root.right:
            self.dfsPathSum2(root.right, sum, curr + [root.val], result)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
print Solution().pathSum(root, 22)