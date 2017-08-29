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
        head = root
        while head:
            nextHead = None
            prev, cur= None, head
            while cur:
                if not nextHead:
                    if cur.left:
                        nextHead = cur.left
                    elif cur.right:
                        nextHead = cur.right
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right
                cur = cur.next
            head = nextHead


root, root.left, root.right = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3)
root.left.left, root.left.right , root.right.right= TreeLinkNode(4), TreeLinkNode(5) , TreeLinkNode(6)
root.left.left.left , root.right.right.right = TreeLinkNode(7), TreeLinkNode(8)
Solution().connect(root)
print root
print root.left
print root.left.left
print root.left.left.left