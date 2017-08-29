class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):

        return self.buildTree(0, len(nums) ,nums)

    def buildTree(self , start , end , nums):
        if start == end:
            return None
        mid = (start + end ) /2
        root = TreeNode ( nums[mid])
        root.left = self.buildTree(start, mid , nums )
        root.right = self.buildTree(mid + 1, end , nums)

        return root

num = [1, 2, 3]
result = Solution().sortedArrayToBST(num)
print result.val
print result.left.val
print result.right.val