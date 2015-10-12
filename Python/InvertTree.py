class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.doInvert(root)
        return root
        
    def doInvert(self, root):
        if root == None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.doInvert(root.left)
        self.doInvert(root.right)
