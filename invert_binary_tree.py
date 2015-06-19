# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		# base case
		if root == None:
			return None
		
		# reverse children sub trees first
		left = root.left
		right = root.right
		
		# swap left and right children
		root.left = self.invertTree(right)
		root.right = self.invertTree(left)
		
		# return root with reverted children
		return root