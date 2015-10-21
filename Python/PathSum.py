# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        self.flag = False
        self.dfs(root, sum, 0)
        return self.flag
        
    def dfs(self, root, sum, prev):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val + prev == sum:
                self.flag = True
        self.dfs(root.left, sum, prev + root.val)
        self.dfs(root.right, sum, prev + root.val)
