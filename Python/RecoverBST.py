# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        import sys
        self.prev = TreeNode(-sys.maxint-1)
        self.firstNode = None
        self.secondNode = None
        self.dfs_preorder(root)
        # shollow swap
        temp = self.firstNode.val
        self.firstNode.val = self.secondNode.val
        self.secondNode.val = temp
        
    def dfs_preorder(self, root):
        if root == None:
            return
        self.dfs_preorder(root.left)
        if root.val < self.prev.val:
            if self.firstNode == None:
                self.firstNode = self.prev
            self.secondNode = root
        self.prev = root
        self.dfs_preorder(root.right)
