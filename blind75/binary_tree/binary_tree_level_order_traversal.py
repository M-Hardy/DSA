# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        bfsOrder = []
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            level = []
            # set num iterations for processing queue as current len 
            # current len = num nodes at current level
            for i in range(len(queue)):
                node = queue.popleft()                            
                level.append(node.val)
                # check node children are not null so you don't append
                # empty nodes to level array/result array
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            bfsOrder.append(level)
            
        return bfsOrder