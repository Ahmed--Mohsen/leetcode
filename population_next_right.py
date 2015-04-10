# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if root == None:
			return
			
		self.connect(root.left)
		self.connect(root.right)
		
		left = root.left
		right = root.right
		
		while left:
			left.next = right
			left = left.right
			right = right.left