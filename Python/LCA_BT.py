class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        left_LCA = self.lowestCommonAncestor(root.left, p, q)
        right_LCA = self.lowestCommonAncestor(root.right, p, q)
        if left_LCA and right_LCA:
            return root
        return left_LCA if left_LCA else right_LCA

    # double recursive, TLE
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None or not self.containsNode(root, p) or not self.containsNode(root, q):
            return None
        if root.val == p.val or root.val == q.val:
            return root            
        left_p, right_p = self.containsNode(root.left, p), self.containsNode(root.right, p)
        left_q, right_q = self.containsNode(root.left, q), self.containsNode(root.right, q)
        if left_p and right_q or left_q and right_p:
            return root
        if left_p and left_q:
            return self.lowestCommonAncestor(root.left, p, q)
        if right_p and right_q:
            return self.lowestCommonAncestor(root.right, p, q)
        
    def containsNode(self, root, node):
        if root is None:
            return False
        if root.val == node.val:
            return True
        return self.containsNode(root.left, node) or self.containsNode(root.right, node)
