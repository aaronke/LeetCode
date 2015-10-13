def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return False
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
  
def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return None
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if fast == slow:
        while head != slow:
            head = head.next
            slow = slow.next
        return head
    else:
        return Nonereturn False
