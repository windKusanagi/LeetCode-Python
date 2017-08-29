
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        result, sum  ,cur = [] , 0 , str(root.val)
        self.sumN ( root, result , cur)
        for s in result:
            sum+= int( s )
        return sum
    def sumN ( self, node , result , cur ):
        if not node.left and not node.right:
            result.append( str(cur))
            return
        if node.left:
            self.sumN( node.left , result , cur + str(node.left.val))
        if node.right:
            self.sumN( node.right , result , cur + str(node.right .val))

n1, n2,n3 , n4 = TreeNode(1) , TreeNode(2) ,TreeNode(3) , TreeNode(4)
n1.left , n1.right = n2 , n3
#n1.left.left = n4
print Solution().sumNumbers(n1)
