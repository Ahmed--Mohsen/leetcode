"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		if root == None: #base case
			return 0
		
		max_left = self.maxDepth(root.left)
		max_right = self.maxDepth(root.right)
		
		return 1 + max(max_left, max_right)
			