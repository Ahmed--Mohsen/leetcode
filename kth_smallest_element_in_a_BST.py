# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
	self.val = x
	self.left = None
	self.right = None

class Solution:
	# @param {TreeNode} root
	# @param {integer} k
	# @return {integer}
	def kthSmallest(self, root, k):
		stack = []
		pointer = root
		index = 0
		
		# move to the most minimum
		while pointer:
			stack.append(pointer)
			pointer = pointer.left
		
		# process each node in stack
		while stack:
			
			# each node is in order
			pointer = stack.pop()
			index += 1
			
			# check if reached k
			if index == k:
				break
			
			# check if right subtree exist
			if pointer.right:
				
				# add the left subtree of the right subtree
				pointer = pointer.right
				while pointer:
					stack.append(pointer)
					pointer = pointer.left
			
		return pointer.val	
		
		