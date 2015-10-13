# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
	"""
	:type root: TreeNode
	:type p: TreeNode
	:type q: TreeNode
	:rtype: TreeNode
	"""
	def lowestCommonAncestor(self, root, p, q):		
		# failed to find LCA or LCA is either of them
		if root in (None, p, q): 
			return root
		
		# look for LCA in the left subtree
		left = self.lowestCommonAncestor(root.left, p, q)
		
		# look for LCA in the right subtree
		right = self.lowestCommonAncestor(root.right, p, q)
		
		# p and q are on either side
		if left and right:
			return root
		
		# LCA is either left or right subtree root
		return left or right
		
		
		