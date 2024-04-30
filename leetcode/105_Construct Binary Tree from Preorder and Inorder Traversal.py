# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {value: idx for idx, value in enumerate(inorder)}

        def array_to_tree(left, right):
            # if there are no element to construct a tree
            if left > right:
                return None

            # select the preorder_index element as the root and increment it
            root_value = preorder.pop(0)
            root = TreeNode(root_value)
            
            # all elements with index < inorder_dict are in the left subtree
            # all elements with index > inorder_dict are in the right subtree
            inorder_idx = inorder_dict[root_value]

            root.left = array_to_tree(left, inorder_idx - 1)
            root.right = array_to_tree(inorder_idx + 1, right)

            return root
        
        return array_to_tree(0, len(inorder) - 1)
