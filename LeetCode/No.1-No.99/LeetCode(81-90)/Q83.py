# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def my_print(self):
        print(self.val)
        if self.next:
            print(self.next.val)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy.next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    '''
    n3 = ListNode(1)
    n4 = ListNode(1)
    n5 = ListNode(2)'''
    n1.next = n2
    '''
    n2.next = n3
    n3.next = n4
    n4.next = n5'''
    r = Solution().deleteDuplicates(n1)
    r.my_print()