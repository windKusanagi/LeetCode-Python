# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myprint(self):
        print(self.val)
        if self.next:
            self.next.myprint()

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        cur = head
        cut = length - k % length
        while cut > 0:
            curr = curr.next
            cut -= 1
        result = curr.next
        curr.next = None
        return result


l1 = ListNode(1)
l2 = ListNode(2)

l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
result = Solution().rotateRight(l1, 6)
result.myprint()

