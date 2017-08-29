import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
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

    def mergeKLists(self, lists):
        if not lists:
            return None
        left = 0
        right = len(lists)-1
        while right > 0:
            if left >= right :
                left = 0
            else:
                lists[left] = self.mergeTwoLists(lists[left] , lists[right])
                left += 1
                right -= 1
        return lists[0]
'''

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        dummy = ListNode(-1)
        head = dummy
        while heap:
            smallestNode = heapq.heappop(heap)[1]
            head.next = smallestNode
            head = head.next
            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, smallestNode.next))
        return dummy.next