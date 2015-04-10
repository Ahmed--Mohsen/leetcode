# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	
	def __init__(self):
		self.path = []

	# @param root, a tree node
	# @return a list of integers
	def preorderTraversal(self, root):
		self.traverse(root)
		return self.path

	def traverse(self, root):
		if root == None:
			return
		#visit root
		self.path.append(root.val)
		
		if root.left != None:
			self.traverse(root.left)
		
		if root.right != None:
			self.traverse(root.right)
			

"""
s = Solution()
t = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t.right = t2
t2.right = t3
print s.preorderTraversal(t)
"""