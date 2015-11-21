"""

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).

"""

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
		
		