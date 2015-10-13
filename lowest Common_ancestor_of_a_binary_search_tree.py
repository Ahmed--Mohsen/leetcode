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
		
		while root:
			# LCA is in the left subtree
			if p.val < root.val > q.val:
				root = root.left
			
			# LCA is in the right subtree
			elif p.val > root.val < q.val:
				root = root.right
			
			# LCA is the root itself
			else:
				return root


	"""
	:type root: TreeNode
	:type p: TreeNode
	:type q: TreeNode
	:rtype: TreeNode
	"""
	def lowestCommonAncestorRecursive(self, root, p, q):
		# LCA is either nodes
		if root.val == p.val or root.val == q.val:
			return root
		
		# LCA is in the left subtree
		if  root.val > p.val and root.val > q.val:
			return self.lowestCommonAncestor(root.left, p, q)
			
		# LCA is in the right subtree
		if  root.val < p.val and root.val < q.val:
			return self.lowestCommonAncestor(root.right, p, q)
		
		# root is in the middle
		return root


