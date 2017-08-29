# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = head
        cur = prev.next
        prev.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        dummy.next = prev
        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
#n2.next = n3
r = Solution().reverseList(n1)
print r.to_list()