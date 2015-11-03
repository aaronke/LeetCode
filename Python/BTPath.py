# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.result = []
        self.dfs(root, '')
        return self.result

    def dfs(self, root, path):
        path += '->' + str(root.val)
        if root.left is None and root.right is None:
            self.result.append(path[2:])
        else:
            if root.left is not None:
                self.dfs(root.left, path)
            if root.right is not None:
                self.dfs(root.right, path)
    # add and remove version, path is list[]
    def dfs(self, root, path):
        path.append(str(root.val))
        if root.left is None and root.right is None:
            self.result.append('->'.join(path))
        else:
            if root.left is not None:
                self.dfs(root.left, path)
            if root.right is not None:
                self.dfs(root.right, path)
        del path[-1]
