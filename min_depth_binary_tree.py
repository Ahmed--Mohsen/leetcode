"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
	def minDepth(self, root):
		# base cases
		if root == None: return 0
		if root.left == None and root.right == None: return 1
		
		# calc min depth for each child
		left_depth =  self.minDepth(root.left)
		right_depth = self.minDepth(root.right)
		
		# the number of nodes along the shortest path from 
		# the root node down to the nearest leaf node
		if left_depth == 0 or right_depth == 0:
			return max(left_depth, right_depth) + 1
		
		# normal case
		return min(left_depth, right_depth) + 1