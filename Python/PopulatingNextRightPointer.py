class Solution(object):
    # look at this guy's coding style and logic, awesome! 
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        current = root
        prev = None
        start = None
        while current != None:
            while current != None:
                # left child
                if current.left != None:
                    if prev == None:
                        prev = current.left
                        start = current.left
                    else:
                        prev.next = current.left
                        prev = current.left
                # right child
                if current.right != None:
                    if prev == None:
                        prev = current.right
                        start = current.right
                    else:
                        prev.next = current.right
                        prev = current.right
                current = current.next
            current = start
            start = None
            prev = None    
