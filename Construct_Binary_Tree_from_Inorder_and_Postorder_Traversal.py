# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		#for helper2 method
		self.root_to_inorder_map = {}
		for i in range(len(inorder)):
			self.root_to_inorder_map[inorder[i]] = i

		#return self.buildTreeHelper(inorder, postorder)
		return self.buildTreeHelper2(inorder, postorder, 0)
		
	
	#takes O(n^2) due to inorder.index takes O(n)
	def buildTreeHelper(self, inorder, postorder):
		if len(inorder) == 0:
			return None
		
		root = TreeNode(postorder[-1])
		divider = inorder.index(root.val)
		root.left = self.buildTreeHelper(inorder[:divider], postorder[:divider])
		root.right = self.buildTreeHelper(inorder[divider+1:], postorder[divider:-1])
		
		return root
		
	
	#take O(n) usage of map instead of inorder.index
	#offset is the starting position of the right subtree index
	def buildTreeHelper2(self, inorder, postorder, offset):
		if len(inorder) == 0:
			return None
		
		root = TreeNode(postorder[-1])
		divider = self.root_to_inorder_map[root.val] - offset
		root.left = self.buildTreeHelper2(inorder[:divider], postorder[:divider], offset )
		root.right = self.buildTreeHelper2(inorder[divider+1:], postorder[divider:-1], offset + divider + 1)
		
		return root