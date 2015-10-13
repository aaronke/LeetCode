# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        slow, fast = head, head
        previous = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow.next, previous, slow = previous, slow, slow.next
        # odd
        if fast != None:
            slow = slow.next
        while slow != None:
            if slow.val != previous.val:
                return False
            slow = slow.next
            previous = previous.next
        return True
