# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenB > lenA:
            for i in range(lenB-lenA):
                headB = headB.next
        else:
            for i in range(lenA-lenB):
                headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
    def getLength(self, head):
        thisLength = 0
        while head:
            thisLength += 1
            head = head.next
        return thisLength
