"""

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param p, a tree node
	# @param q, a tree node
	# @return a boolean
	def isSameTree(self, p, q):
		# both have no children
		if (p == None) and (q == None): 
			return True
			
		# one has children while other not (XOR)
		if (p == None) != (q == None): 
			return False
		
		# roots are matched checking further levels
		if p.val == q.val: 
			same_left = self.isSameTree(p.left, q.left)
			same_right = self.isSameTree(p.right, q.right)
			return same_left & same_right
		else:
			return False