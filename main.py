# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: If the tree is empty, return 0
        if root is None:
            return 0
        
        # Recursive case: Compute the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return the maximum of the two depths plus 1 for the current node
        return max(left_depth, right_depth) + 1
