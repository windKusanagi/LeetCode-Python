# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        for __ in range(m - 1):
            start = start.next
        prev = start.next
        curr = prev.next
        for __ in range(n - m):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        print curr.val
        print start.val, start.next.val, start.next.next.val
        start.next.next = curr
        start.next = prev
        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
r = Solution().reverseBetween(n1, 2, 4)
print r.to_list()