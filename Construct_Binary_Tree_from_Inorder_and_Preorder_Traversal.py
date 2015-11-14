"""

Given preorder and inorder traversal of a tree, construct the binary tree.

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
	# @param preorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		
		# cache each element index
		inorder_map = {} # key = node value, value = node index
		for i in range(len(inorder)):
			inorder_map[inorder[i]] = i
			
		return self.buildTreeHelper(inorder,0, len(inorder) - 1, preorder, 0, len(preorder) - 1, inorder_map)
		
	
	# takes O(n) usage of map instead of inorder.index
	# offset is the starting position of the right subtree index
	def buildTreeHelper(self, inorder, in_start, in_end ,preorder, pre_start, pre_end, inorder_map):
		# base case
		if in_start > in_end or pre_start > pre_end:
			return None
		
		# root is always first node in preorder 
		root = TreeNode(preorder[pre_start])
		
		divider = inorder_map[root.val]
		
		# right subtree length
		right_len = divider - in_start
		root.left = self.buildTreeHelper(inorder, in_start, divider-1, preorder, pre_start+1, pre_start+right_len, inorder_map)
		root.right = self.buildTreeHelper(inorder, divider+1, in_end, preorder, pre_start+right_len+1, pre_end, inorder_map)
		
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
		
	
	#takes O(n^2) due to inorder.index takes O(n)
	#Got TLE with this
	def buildTreeHelperSlow(self, preorder, inorder):
		if len(inorder) == 0:
			return None
		print preorder, inorder
		root = TreeNode(preorder[0])
		divider = inorder.index(root.val)
		root.left = self.buildTreeHelper(preorder[1:divider+1], inorder[:divider])
		root.right = self.buildTreeHelper(preorder[divider+1:], inorder[divider+1:])
		
		return root
		

s = Solution()
print s.buildTree([1,2], [2,1])
