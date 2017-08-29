class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = cur.next.next

        return dummy.next
