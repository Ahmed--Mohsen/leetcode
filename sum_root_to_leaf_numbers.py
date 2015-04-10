# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def sumNumbers(self, root):
		return self.preorder_traverse_tree(root, 0)

		
	
	def preorder_traverse_tree(self, root, val):
		#base case 
		if root == None:
			return 0
			
		val = val*10 + root.val
		
		#return if leaf node
		if root.left == None and root.right == None:
			return val
		
		return self.preorder_traverse_tree(root.left, val) + self.preorder_traverse_tree(root.right, val)
		
s = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
print s.sumNumbers(r)