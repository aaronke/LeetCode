# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(head.val+1)
        dummy.next = head
        runner = dummy
        while runner.next != None:
            if runner.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return dummy.next
