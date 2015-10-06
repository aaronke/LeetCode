# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# reverse, then adjust left and right bound
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cycle = self.getLength(head)/k
        if cycle == 0 or k <= 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        previous_node = dummy
        current_node = head
        next_node = head.next
        for i in range(cycle):
            left = previous_node
            for j in range(k):
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
                if next_node != None:
                    next_node = next_node.next
            right = left.next
            right.next = current_node
            left.next = previous_node
            previous_node = right
        return dummy.next
            
    def getLength(self, head):
        i = 0
        while head != None:
            head = head.next
            i += 1
        return i
