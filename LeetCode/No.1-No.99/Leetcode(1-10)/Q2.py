#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        current = result
        while l1 or l2:
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next

            if current.val >= 10:
                current.next = ListNode(1)
                current.val -= 10
            elif l1 or l2:
                current.next = ListNode(0)

            current = current.next

        return result

if __name__ == '__main__':
    x, x.next, x.next.next = ListNode(2), ListNode(4), ListNode(3)
    y, y.next, y.next.next  =  ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(x, y)
    print result


