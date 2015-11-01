class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None:
            return None
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if root.val >= p.val and root.val <= q.val:
            return root
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
