# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a tree node
	def recoverTree(self, root):
		self.first = None
		self.second = None
		self.prev = None
		
		self.traverse(root)
		self.swap(self.first, self.second)
		
		return root
	
	#in order traversal with prev as pointer
	def traverse(self, root):
		if root == None:
			return
		
		self.traverse(root.left)
		if self.prev != None:
			if self.prev.val >= root.val:
				if self.first == None:
					self.first = self.prev
				self.second = root
		self.prev = root
		self.traverse(root.right)
	
	def swap(self, node1, node2):
		temp = node1.val
		node1.val = node2.val
		node2.val = temp