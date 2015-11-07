"""

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

"""

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
			self.current_max = float("-inf")
			self.traverse_tree(root)
			return self.current_max
	
	def traverse_tree(self, root):
		if root == None:
			return 0
		
		# calc left max
		left_max = max(0, self.traverse_tree(root.left))
		
		# calc right max
		right_max = max(0, self.traverse_tree(root.right))
		
		# update current_max
		root_max_sum = root.val + left_max + right_max
		self.current_max = max(self.current_max, root_max_sum)
		
		#return the max path sum from this root
		return max(left_max, right_max) + root.val