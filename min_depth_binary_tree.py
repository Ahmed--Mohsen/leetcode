# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def minDepth(self, root):
		if root == None:
			return 0
		if root.left == None and root.right == None:
			return 1
		
		min_depth_val = float("inf")
		if root.left:
			min_depth_val = min(min_depth_val, self.minDepth(root.left) + 1)
		if root.right:
			min_depth_val = min(min_depth_val, self.minDepth(root.right) + 1)
		
		return min_depth_val