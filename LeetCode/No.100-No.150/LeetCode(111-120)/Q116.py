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
        cur = []
        cur.append(root)
        if root:
            while cur:
                nextlevel =[]
                for i,n in enumerate(cur):
                    if n.left:
                        nextlevel.append(n.left)
                    if n.right:
                        nextlevel.append(n.right)
                    if i<len(cur)-1:
                        n.next = cur[i+1]
                cur = nextlevel


root, root.left, root.right = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3)
root.left.left, root.left.right, root.right.left, root.right.right = TreeLinkNode(4), \
                                  TreeLinkNode(5), TreeLinkNode(6), TreeLinkNode(7)
Solution().connect(root)
print root
print root.left
print root.left.left