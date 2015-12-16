"""

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		return self.isValidBSTHelper(root, float("-inf"), float("inf"))
		
	
	def isValidBSTHelper(self, root, min, max):
		# base case
		if root == None: 
			return True
		
		# root must lay between the boundries
		if root.val < min or root.val > max:
			return False
		
		return self.isValidBSTHelper(root.left, min, root.val - 1) and self.isValidBSTHelper(root.right, root.val + 1, max)