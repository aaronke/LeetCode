# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        runner = dummy
        for i in range(m-1):
            runner = runner.next
        left = runner # left bound before reverse range
        previous_node = runner
        runner = runner.next # first node to reverse
        for i in range(n-m+1):
            temp = runner.next
            runner.next = previous_node
            previous_node = runner
            runner = temp
        left.next.next = runner # reversed head to tail
        left.next = previous_node # tail to head
        return dummy.next
