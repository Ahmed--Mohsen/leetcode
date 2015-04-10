# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxPathSum(self, root):
			self.current_max = 0
			if root != None:
				self.current_max = root.val
				self.traverse_tree(root)
			return self.current_max
	
	def traverse_tree(self, root):
		if root == None:
			return 0
		
		#calc left max
		left_max = self.traverse_tree(root.left)
		
		#calc right max
		right_max = self.traverse_tree(root.right)
		
		#update current_max
		current_max_sum = root.val
		if left_max > 0:
			current_max_sum += left_max
		if right_max > 0:
			current_max_sum += right_max
		self.current_max = max(self.current_max, current_max_sum)
		
		#return the max path sum from this root
		return max(root.val, root.val + left_max, root.val + right_max)