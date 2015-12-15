"""

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

"""

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
		self.prev = TreeNode(float("-inf"))
		
		self.traverse(root)
		self.swap(self.first, self.second)
		
	
	# in order traversal with prev as pointer
	def traverse(self, root):
		# base case
		if root == None: return
			
		# visit left child
		self.traverse(root.left)
		
		# visit root
		# set first pointer if not set
		if self.first == None and self.prev.val >= root.val:
			self.first = self.prev
			
		# set second pointer if first not set
		if self.first != None and self.prev.val >= root.val:
			self.second = root
		
		self.prev = root
		
		# visit right child
		self.traverse(root.right)
	
	def swap(self, node1, node2):
		temp = node1.val
		node1.val = node2.val
		node2.val = temp