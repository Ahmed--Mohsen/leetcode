"""

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

"""

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
		
		# cache each element index
		inorder_map = {} # key = node value, value = node index
		for i in range(len(inorder)):
			inorder_map[inorder[i]] = i
			
		return self.buildTreeHelper(inorder,0, len(inorder) - 1, postorder, 0, len(postorder) - 1, inorder_map)
				
	
	
	
	# takes O(n) usage of map instead of inorder.index
	# offset is the starting position of the right subtree index
	def buildTreeHelper(self, inorder, in_start, in_end ,postorder, post_start, post_end, inorder_map):
		# base case
		if in_start > in_end or post_start > post_end:
			return None
		
		# root is always last node in postorder 
		root = TreeNode(postorder[post_end])
		
		divider = inorder_map[root.val]
		
		# right subtree length
		right_len = divider - in_start
		root.left = self.buildTreeHelper(inorder, in_start, divider-1, postorder, post_start, post_start+right_len-1, inorder_map)
		root.right = self.buildTreeHelper(inorder, divider+1, in_end, postorder, post_start+right_len, post_end - 1, inorder_map)
		
		return root
		

	# takes O(n^2) due to inorder.index takes O(n)
	def buildTreeHelperSlow(self, inorder, postorder):
		if len(inorder) == 0:
			return None
		
		root = TreeNode(postorder[-1])
		divider = inorder.index(root.val)
		root.left = self.buildTreeHelper(inorder[:divider], postorder[:divider])
		root.right = self.buildTreeHelper(inorder[divider+1:], postorder[divider:-1])
		
		return root
