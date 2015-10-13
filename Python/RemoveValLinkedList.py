class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return
        dummy = ListNode(-1)
        dummy.next = head
        runner = dummy
        while runner.next != None:
            if runner.next.val == val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return dummy.next
