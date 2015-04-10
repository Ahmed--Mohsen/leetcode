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
		if (p == None) and (q == None): #both have no children
			return True
			
		if (p == None) != (q == None): #one has children while other not (XOR)
			return False
		
		if p.val == q.val: #roots are matched checking further levels
			same_left = self.isSameTree(p.left, q.left)
			same_right = self.isSameTree(p.right, q.right)
			return same_left & same_right
		else:
			return False