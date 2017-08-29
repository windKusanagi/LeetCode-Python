# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    def __repr__(self):
        if self is None:
            return "Null"
        else:
            return "{} -> {}".format(self.val, repr(self.next))
class Solution:
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)


root, root.left, root.right = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3)
root.left.left, root.left.right, root.right.left, root.right.right = TreeLinkNode(4), \
                                  TreeLinkNode(5), TreeLinkNode(6), TreeLinkNode(7)
Solution().connect(root)
print root
print root.left
print root.left.left