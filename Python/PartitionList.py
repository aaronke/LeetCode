# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        partition_left, partition_right, runner = dummy, dummy, dummy
        # locate the partition point
        while partition_left.next != None:
            if partition_left.next.val >= x:
                break
            partition_left = partition_left.next
        partition_right = partition_left.next
        runner = partition_right
        # partition begin
        while runner != None and runner.next != None:
            if runner.next.val < x:
                partition_left.next = runner.next
                partition_left = partition_left.next
                runner.next = runner.next.next
            else:
                runner = runner.next
        partition_left.next = partition_right
        return dummy.next
