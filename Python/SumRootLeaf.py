# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.nums = []
        self.dfs(root, 0)
        return sum(self.nums)
        
    def dfs(self, root, prev):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.nums.append(prev*10+root.val)
        self.dfs(root.left, prev*10+root.val)
        self.dfs(root.right, prev*10+root.val)
