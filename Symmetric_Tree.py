# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		if root == None:
			return True
			
		return self.isSymmetricHelper(root.left, root.right)
	
	
	def isSymmetricHelper(self, left, right):
		if (left == None) and (right == None): #both have no children
			return True
			
		if (left == None) != (right == None): #one has children while other not (XOR)
			return False
		
		if left.val == right.val: #roots are matched checking further levels
			inner_mirror = self.isSymmetricHelper(left.right, right.left)
			outer_mirror = self.isSymmetricHelper(left.left, right.right)
			return inner_mirror & outer_mirror
		else:
			return False