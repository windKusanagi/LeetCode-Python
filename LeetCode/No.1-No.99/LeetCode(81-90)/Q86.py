class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution(object):
    def partition(self, head, x):
        dummy = ListNode(-1)
        if not head :
            return dummy.next
        small = ListNode(-1)
        large = ListNode(-1)
        curS = small
        curL = large
        cur = head
        while cur:
            if cur.val < x:
                curS.next = cur
                curS = curS.next
            else:
                curL.next = cur
                curL = curL.next
            cur = cur.next
        curL.next = None
        curS.next = large.next
        dummy.next = small.next
        return dummy.next


n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
r = Solution().partition(n1, 3)
print r.to_list()

