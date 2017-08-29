class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 or l2:
            if l1:
                if l2:
                    if l1.val>l2.val:
                        cur.next = ListNode(l2.val)
                        l2 = l2.next
                        cur = cur.next
                    else:
                        cur.next = ListNode(l1.val)
                        l1 = l1.next
                        cur = cur.next
                else:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                    cur = cur.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
                cur = cur.next
        return dummy.next;

l1 = ListNode(0)
l1.next = ListNode(2)
l1.next.next = ListNode(5)
l2 = ListNode (1)
l2.next = ListNode(3)

print Solution().mergeTwoLists(l1,l2).val;
print Solution().mergeTwoLists(l1,l2).next.val;
print Solution().mergeTwoLists(l1,l2).next.next.val;
print Solution().mergeTwoLists(l1,l2).next.next.next.val;
print Solution().mergeTwoLists(l1,l2).next.next.next.next.val;