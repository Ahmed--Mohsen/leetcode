# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		
		# base case
		if root == None:
			return
		
		# traverse the tree while there is a left child
		pointer = root
		while pointer.left:
			current = pointer
			
			while current:
				
				# inner link
				current.left.next = current.right
				
				# outer link
				if current.next:
					current.right.next = current.next.left
					
				# move to next sibling on same level
				current = current.next
			
			# move to next child 
			pointer = pointer.left
	
	
	
	########################### Another Solution (REcursive) ###########################
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if root == None:
			return
			
		self.connect(root.left)
		self.connect(root.right)
		
		left = root.left
		right = root.right
		
		while left:
			left.next = right
			left = left.right
			right = right.left