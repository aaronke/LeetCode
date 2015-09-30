class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        self.max = -sys.maxint-1
        self.rootPathSum(root)
        return self.max
        
    def rootPathSum(self, root):
        if root == None:
            return 0
        left = max(0, self.rootPathSum(root.left))
        right = max(0, self.rootPathSum(root.right))
        self.max = max(self.max, root.val+left+right)
        return root.val + max(left, right)
