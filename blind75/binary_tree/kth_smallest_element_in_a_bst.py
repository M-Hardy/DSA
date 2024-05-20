# for recursive solution - easiest to keep state
# of result variables outside of recursive function 
# entirely so it makes updating as you recursively
# traverse through the tree much easier.
#
# initially tried solving it using dfs using an 
# approach similar to the maxDepth problem, but 
# i kept returning None - couldn't figure out a 
# way to 'bubble up' the result node/value immediately once
# i found it; it's worth exploring why it's easy for maxDepth 
# but not this problem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #NC ITERATIVE SOLUTION
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            else:
                cur = cur.right
        return None
    
    
    def recursiveKthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.res = None

        def dfs(root, k):
            if self.res:
                return
            if not root:
                return
            dfs(root.left, k) 
            self.count += 1
            if self.count == k:
                self.res = root.val
                return 
            dfs(root.right, k) 

        dfs(root, k)
        return self.res 