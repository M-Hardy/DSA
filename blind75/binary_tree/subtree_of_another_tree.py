"""
NC conditions (for isSubtree) make it a bit more semantically clear:
- if subRoot is empty tree, then a subtree exists by default (empty node)
- if root is empty tree, then a subtree cannot exist by default 

if not t:
    return True
if not s:
    return False
    
if self.isSameTree(root, subRoot): 
    ...
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        if not root and subRoot:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        
        
    def isSameTree(self, p, q):
        
        if not p and not q:
            return True
        
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)