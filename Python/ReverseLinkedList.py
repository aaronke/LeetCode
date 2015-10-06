# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        previous_node = None
        current_node = head
        next_node = head.next
        while next_node != None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = previous_node
        return current_node

# recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.result = None
        self.reverse(head)
        return self.result
        
    def reverse(self, head):
        if head == None:
            return
        if head.next == None:
            self.result = head
            return
        self.reverse(head.next)
        head.next.next = head
        head.next = None
