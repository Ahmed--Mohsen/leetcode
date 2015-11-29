# -*- coding: utf-8 -*-
"""

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

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
		
		
		