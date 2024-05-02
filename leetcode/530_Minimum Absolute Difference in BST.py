# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node, prev_val, min_diff):
            if node is None:
                return min_diff, prev_val

            min_diff, prev_val = inorder_traversal(node.left, prev_val, min_diff)

            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)

            prev_val = node.val 

            min_diff, prev_val = inorder_traversal(node.right, prev_val, min_diff)

            return min_diff, prev_val
        
        min_diff, _ = inorder_traversal(root, None, 100001)
        return min_diff
