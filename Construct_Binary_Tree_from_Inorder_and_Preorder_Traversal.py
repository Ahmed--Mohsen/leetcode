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
	def buildTree(self, preorder, inorder):
		#for helper2 method
		self.root_to_inorder_map = {}
		for i in range(len(inorder)):
			self.root_to_inorder_map[inorder[i]] = i

		#return self.buildTreeHelper(preorder, inorder)
		return self.buildTreeHelper2(preorder, inorder, len(inorder), 0)
		
	
	#takes O(n^2) due to inorder.index takes O(n)
	#Got TLE with this
	def buildTreeHelper(self, preorder, inorder):
		if len(inorder) == 0:
			return None
		print preorder, inorder
		root = TreeNode(preorder[0])
		divider = inorder.index(root.val)
		root.left = self.buildTreeHelper(preorder[1:divider+1], inorder[:divider])
		root.right = self.buildTreeHelper(preorder[divider+1:], inorder[divider+1:])
		
		return root
		
	
	#takes O(n) due to usage of map instead of inorder.index
	#offset is the starting position of the right subtree index in the inorder list
	def buildTreeHelper2(self, preorder, inorder, n, offset):
		if n == 0:
			return None
		
		root = TreeNode(preorder[0])
		divider = self.root_to_inorder_map[root.val] - offset
		root.left = self.buildTreeHelper2(preorder[1:divider+1], inorder[:divider], divider, offset )
		root.right = self.buildTreeHelper2(preorder[divider+1:], inorder[divider+1:], n-divider-1, offset + divider + 1)
		
		return root

s = Solution()
print s.buildTree([1,2], [2,1])
