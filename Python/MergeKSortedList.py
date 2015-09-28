class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists) < 1:
            return None
        while len(lists) > 1:
            first = 0
            last = len(lists) - 1
            while first < last:
                if lists[first] == None:
                    lists.pop(first)
                    last -= 1
                    continue
                if lists[last] == None:
                    lists.pop(last)                    
                    last -= 1
                    continue                
                lists[first] = self.merge_two(lists[first], lists[last])
                first += 1
                last -= 1
                lists.pop(-1)
        return lists[0]

    def merge_two(self, first, last):
        head = ListNode(-1)
        runner = ListNode(-1)
        if first.val <= last.val:
            head.next = first
        else:
            head.next = last
        while first != None and last != None:
            if first.val <= last.val:
                runner.next = first
                runner = first
                first = first.next
            else:
                runner.next = last
                runner = last
                last = last.next
        if first != None:
            runner.next = first
        elif last != None:
            runner.next = last
        return head.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            n = len(lists)
            for i in range(n/2):
                lists[i] = self.merge2(lists[i],lists[-1-i])
            lists = lists[:n/2+n%2]
        return lists[0]
        
    def merge2(self, node1, node2):
        if node1 == None and node2 == None:
            return None
        if node1 == None:
            return node2
        if node2 == None:
            return node1
        dummy = ListNode(-1)
        dummy.next = node1 if node1.val<=node2.val else node2
        result = dummy.next
        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                dummy.next = node1
                node1 = node1.next
            else:
                dummy.next = node2
                node2 = node2.next
            dummy = dummy.next
        dummy.next = node1 if node1 != None else node2
        return result
