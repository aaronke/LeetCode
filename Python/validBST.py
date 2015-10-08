# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative check in-order traversal, most efficient, O(N)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        stack = []
        stack.append(root)
        while root.left != None:
            root = root.left
            stack.append(root)
        import sys
        prev = -sys.maxint-1
        while len(stack) != 0:
            node = stack.pop()
            if node.val <= prev:
                return False
            else:
                prev = node.val
            if node.right != None:
                node = node.right
                stack.append(node)
                while node.left != None:
                    node = node.left
                    stack.append(node)
        return True
# recursive in-order
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        import sys
        self.prev = -sys.maxint-1
        self.flag = True
        self.inorder(root)
        return self.flag
    
    def inorder(self, root):
        if root == None or self.flag == False:
            return
        self.inorder(root.left)
        if root.val <= self.prev:
            self.flag = False
        else:
            self.prev = root.val
        self.inorder(root.right)

# check root.val with left subtree max, and right sub-tree min
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left != None:
            runner = root.left
            while runner.right != None:
                runner = runner.right
            if runner.val >= root.val:
                return False
        if root.right != None:
            runner = root.right
            while runner.left != None:
                runner = runner.left
            if runner.val <= root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        

# recursive check max, min
    import sys
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.helper(root, -sys.maxint - 1, sys.maxint)

    def helper(self, root, mini, maxm):
        if root == None:
            return True
        return root.val > mini and root.val < maxm and self.helper(root.left,mini,root.val) 
        and self.helper(root.right,root.val,maxm)
