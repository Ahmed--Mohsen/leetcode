"""

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		#self.traversal = []
		#self.inorderTraversalHelper(root)
		#return self.traversal
		return self.inorderTraversalHelper2(root)
	
	
	# recursive solution
	def inorderTraversalHelper(self, root):
		if root == None:
			return
		
		if root.left:
			self.inorderTraversalHelper(root.left)
			
		self.traversal.append(root.val)
		
		if root.right:
			self.inorderTraversalHelper(root.right)
	
	# iterative solution
	def inorderTraversalHelper2(self, root):
		if root == None:
			return []
							
		traversal = []
		stack = [root]
		visited = set()
		
		while len(stack) > 0:
			current = stack.pop()
			
			if current in visited:
				traversal.append(current.val)
				continue
				
			visited.add(current)
			
			if current.right: # visit left subtree
				stack.append(current.right)
				
			stack.append(current)
			
			if current.left:
				stack.append(current.left)
			
		return traversal
				
				
				
