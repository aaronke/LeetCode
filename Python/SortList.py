# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        mid = self.findMid(head)
        head2 = mid.next
        mid.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(head2)
        return self.merge(head1, head2)
        
    def merge(self, head1, head2):
        dummy = ListNode(-1)
        runner = dummy
        while head1 and head2:
            if head1.val < head2.val:
                runner.next = head1
                head1 = head1.next
            else:
                runner.next = head2
                head2 = head2.next
            runner = runner.next
        if head1:
            runner.next = head1
        if head2:
            runner.next = head2
        return dummy.next

    def findMid(self, head):
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
