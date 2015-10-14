# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return
        reverse_head = self.reverse_half(head)
        while reverse_head:
            tmp = head.next
            tmp2 = reverse_head.next
            head.next = reverse_head
            reverse_head.next = tmp
            head = tmp
            reverse_head = tmp2
        
    def reverse_half(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        slow.next, slow = None, slow.next
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        return prev
