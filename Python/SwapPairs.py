# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        runner = dummy
        while runner.next != None and runner.next.next != None:
            # R->A->B>N
            temp_A = runner.next
            runner.next = temp_A.next
            temp_N = runner.next.next
            runner.next.next = temp_A
            temp_A.next = temp_N
            runner = temp_A
        return dummy.next
