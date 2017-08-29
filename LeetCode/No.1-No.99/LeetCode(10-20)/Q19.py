class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pointer1, pointer2 = dummy, dummy

        for i in range(n):
            pointer1 = pointer1.next

        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        pointer2.next = pointer2.next.next
        return dummy.next

n5 = ListNode(5)
n4 = ListNode(4)
n3 = ListNode(3)
n2 = ListNode(2)
n1 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
Solution().removeNthFromEnd(n1, 1).myPrint()

