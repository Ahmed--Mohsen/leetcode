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
			
		left = root.left
		right = root.right
		root.left = None    # Truncate the left subtree
		current = root
		
		# Flatten the left subtree
		current.right = self.flattenHelper(left)
		while current.right:
			current = current.right
			
		# Flatten the right subtree
		current.right = self.flattenHelper(right)
		
		return root