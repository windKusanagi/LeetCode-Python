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
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        flag = 0
        while cur.next:
            while cur.next.next and cur.next.val == cur.next.next.val:
                flag = 1
                cur.next.next = cur.next.next.next
            if flag == 1:
                cur.next = cur.next.next
                flag = 0
            else:
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)

    n3 = ListNode(2)
    '''
    n4 = ListNode(1)
    n5 = ListNode(2)
    '''
    n1.next = n2
    n2.next = n3

    '''
    n3.next = n4
    n4.next = n5
    '''
    r = Solution().deleteDuplicates(n1)
    r.my_print()