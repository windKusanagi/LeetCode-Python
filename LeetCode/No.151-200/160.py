# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        tA, tB = None, None
        while 1:
            if not pA:
                pA = headB

            if not pB:
                pB = headA

            if not pA.next:
                tA = pA
            if not pB.next:
                tB = pB

            if tA and tB and not tA.val == tB.val:
                return None


            if pA.val == pB.val:
                return pA

            pA = pA.next
            pB = pB.next


#A = {1,3,7,10,11} and B = {3,10,11}
if __name__ == '__main__':
    # A = {1,3,7,10,11} and B = {3,10,11}
    # a1, a2, a3, a4, a5 = ListNode(1), ListNode(3), ListNode(7), ListNode(10), ListNode(11)
    # b1, b2, b3 = ListNode(3), ListNode(10), ListNode(11)
    # a1.next, a2.next, a3.next, a4.next, a5.next = a2, a3, a4, a5, None
    # b1.next, b2.next, b3.next = b2, b3, None
    a1, b1 = ListNode(1), ListNode(1)
    a1.next = None
    b1.next = None
    print Solution().getIntersectionNode(a1, b1)
