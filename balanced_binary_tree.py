# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		if root == None:
			return True
		self.balanced = True
		self.isBalancedHelper(root)
		return self.balanced
	
	def isBalancedHelper(self, root):
		if root == None:
			return 0
		left_height = self.isBalancedHelper(root.left)
		right_height = self.isBalancedHelper(root.right)
		self.balanced &= (abs(left_height - right_height) <= 1)
		return max(left_height,right_height) + 1