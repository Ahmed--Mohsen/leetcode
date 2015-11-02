# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		
		# base case
		if root == None:
			return
		
		# simulating level order BFS using the next pointer
		current = root # the head of the current level
		head = TreeNode(-1) # the head of the next level
		tail = head # the tail of the next level
		
		while current:
		
			# check left child
			tail.next = current.left
			if tail.next:
				tail = tail.next
				
			# check right child
			tail.next = current.right
			if tail.next:
				tail = tail.next
			
			# move to next node in the current level
			current = current.next
			
			# check if current level is done (no more nodes)
			# head points to the first node in the next level
			if not current: # reset head and tail
				tail = head
				current = head.next