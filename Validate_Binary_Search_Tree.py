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
		if root == None: #base case
			return True
			
		if root.val < min or root.val > max:
			return False
		
		return self.isValidBSTHelper(root.left, min, root.val - 1) and self.isValidBSTHelper(root.right, root.val + 1, max)