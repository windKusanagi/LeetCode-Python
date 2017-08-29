class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        nums = self.buildSortedArray(head)
        return self.buildTree(0, len(nums) ,nums)

    def buildSortedArray (self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def buildTree(self , start , end , nums):
        if start == end:
            return None
        mid = (start + end ) /2
        root = TreeNode ( nums[mid])
        root.left = self.buildTree(start, mid , nums )
        root.right = self.buildTree(mid + 1, end , nums)

        return root

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
result = Solution().sortedListToBST(head)
print result.val
print result.left.val
print result.right.val