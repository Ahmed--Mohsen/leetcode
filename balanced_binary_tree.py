"""

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

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