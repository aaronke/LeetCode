# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root == None:
            return
        self.__update_stack__(root)
        
    def __update_stack__(self, root):
        while root.left != None:
            self.stack.append(root)
            root = root.left
        self.stack.append(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right != None:
            self.__update_stack__(node.right)
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
