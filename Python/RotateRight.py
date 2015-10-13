# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:
            return head
        size = 0
        run = head
        while run!=None:
            run = run.next
            size += 1
        k = k%size
        fast, slow = head, head
        for i in range(k):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
