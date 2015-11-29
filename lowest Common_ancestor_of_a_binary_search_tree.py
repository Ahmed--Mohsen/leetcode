# -*- coding: utf-8 -*-
"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

"""
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

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


