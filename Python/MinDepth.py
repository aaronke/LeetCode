# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.getMin(root)

    def getMin(self, root):
        import sys
        if root == None:
            return sys.maxint        
        if root.left == None and root.right == None:
            return 1
        return min(self.getMin(root.left), self.getMin(root.right)) + 1
