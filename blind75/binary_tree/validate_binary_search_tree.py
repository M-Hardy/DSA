# need to keep track of lower and upper bounds for 
# each node as we go through the BST. we can't just 
# compare children values to values of immediate parent - 
# a node must be greater than all nodes above it to its left,
# and lesser than all nodes above it to its right.
#
# if a node has nodes above it to both its right AND left, then 
# it has to be greater and lesser than its most recent left and 
# right parents correspondingly. 
#
# so - a node needs to know the most recent parents to its right 
# and left in order for it to know if its value is valid or not in
# the entire tree, not just its immediate parent. 
#
# therefore, every time we go to a child node, we update its most
# recent left/right parent. if we move left, then we have a new most 
# recent right parent, and we update the upper bound as the current node
# - i.e. all nodes to the left of this node must now be lower than this node
# similarly, if we move right, we have a new most recent left parent,
# and we update the lower bound as the current node - i.e. all nodes
# to the right of this node must now be greater than this node
# we pass the current node as the left/right bound depending on the 
# child node so it has the most recent left/right bound to determine
# its validity

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def valid(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float('-inf'), float('inf'))