# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(head.val+1)
        dummy.next = head
        runner = dummy
        while runner.next != None and runner.next.next != None:
            if runner.next.val == runner.next.next.val:
                while runner.next.next != None and runner.next.val == runner.next.next.val:
                    runner.next = runner.next.next
                runner.next = runner.next.next
            else:
                runner = runner.next
        return dummy.next        
        
// BLOW is from last year, 2014        
// get stucked in [1,1,2,2] case, oh my gosh, but after drink a cup of water, a brillient idea comes up, i add an else in line 33, accpted!
public ListNode deleteDuplicates(ListNode head) {
    if (head == null || head.next == null)
        return head;
    // three lines dummy & head exchange
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    head = dummy;
    // when you check head.next.next, always check head.next first, becaue sometimes you may move two steps ahead inside the loop
    while (head.next != null && head.next.next != null) {
        if (head.next.val == head.next.next.val) {
        	// move to the first one whose value is different with the duplicates
            while (head.next.next != null && head.next.val == head.next.next.val)
                head.next = head.next.next;
            head.next = head.next.next;
        }
        else
            head = head.next;
    }
    return dummy.next;
}        
