"""

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	
	# @param {TreeNode} root
	# @return {integer}
	def countNodes(self, root):
		
		# base case
		if root == None:	return 0
		
		# max height from left
		height_left = 0
		left = root
		while left:
			height_left += 1
			left = left.left
			
		# max hight from right
		height_right = 0
		right = root
		while right:
			height_right += 1
			right = right.right
			
		# check if root holding a perfect tree ... (2^h - 1) nodes
		if height_left == height_right:
			return pow(2, height_left) - 1
		
		# not perfect tree case 
		return 1 + self.countNodes(root.left) + self.countNodes(root.right)