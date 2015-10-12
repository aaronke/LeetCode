def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if len(preorder) != len(inorder) or len(preorder) < 1:
        return None
    return self.buildHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
def buildHelper(self, preorder, p_start, p_end, inorder, i_start, i_end):
    if p_start > p_end:
        return None
    root = TreeNode(preorder[p_start])
    divide_gap = self.getGap(root.val, inorder, i_start, i_end)
    root.left = self.buildHelper(preorder, p_start+1, p_start+divide_gap, inorder, i_start, i_start+divide_gap-1)
    root.right = self.buildHelper(preorder, p_start+divide_gap+1, p_end, inorder, i_start+divide_gap+1, i_end)
    return root

def getGap(self, val, inorder, i_start, i_end):
    for i in range(i_start, i_end+1):
        if inorder[i] == val:
            return i-i_start
    return -1

def buildTree(self, inorder, postorder):
    if len(postorder) != len(inorder) or len(postorder) < 1:
        return None
    return self.buildHelper(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1)
    
def buildHelper(self, postorder, p_start, p_end, inorder, i_start, i_end):
    if p_start > p_end:
        return None
    root = TreeNode(postorder[p_end])
    divide_gap = self.getGap(root.val, inorder, i_start, i_end)
    root.left = self.buildHelper(postorder, p_start, p_start+divide_gap-1, inorder, i_start, i_start+divide_gap-1)
    root.right = self.buildHelper(postorder, p_start+divide_gap, p_end-1, inorder, i_start+divide_gap+1, i_end)
    return root

def getGap(self, val, inorder, i_start, i_end):
    for i in range(i_start, i_end+1):
        if inorder[i] == val:
            return i-i_start
    return -1
    
