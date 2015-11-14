"""

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	
	# @param root, a tree node
	# @return nothing, do it in place
	def flatten(self, root):
		self.flattenHelper(root)
	
	def flattenHelper(self, root):
		if root == None:
			return None
		
		# keep track of the subtrees roots	
		left = root.left
		right = root.right
		current = root
		
		# Truncate the left subtree
		root.left = None    

		
		# Flatten the left subtree
		current.right = self.flattenHelper(left)
		while current.right:
			current = current.right
			
		# Flatten the right subtree
		current.right = self.flattenHelper(right)
		
		return root