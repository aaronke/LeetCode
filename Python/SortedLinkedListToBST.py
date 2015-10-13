# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
# getKth is cost O(N), so the total cost is O(N^2)
# but, we can keep a global cursor to build the tree bottem up, avoid retrieving index. 
# (retrieve index in Array is constant, so it doesn't matter)
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        self.cursor = head
        length = self.getLength(head)
        return self.buildTree(head, 0, length-1)
        
    def buildTree(self, head, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        left = self.buildTree(head, start, mid-1)
        root = TreeNode(self.cursor.val)
        self.cursor = self.cursor.next
        right = self.buildTree(head, mid+1, end)
        root.left = left
        root.right = right
        return root
        
    def getLength(self, head):
        thisLength = 0
        while head:
            thisLength += 1
            head = head.next
        return thisLength
        
    # naive recursive    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        length = self.getLength(head)
        return self.buildTree(head, 0, length-1)
        
    def buildTree(self, head, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        root = TreeNode(self.getKth(head, mid).val)
        root.left = self.buildTree(head, start, mid-1)
        root.right = self.buildTree(head, mid+1, end)
        return root

    def getKth(self, head, k):
        for i in range(k):
            head = head.next
        return head
        
    def getLength(self, head):
        thisLength = 0
        while head:
            thisLength += 1
            head = head.next
        return thisLength        
