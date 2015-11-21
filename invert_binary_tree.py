# -*- coding: utf-8 -*-
"""

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

"""

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		# base case
		if root == None:
			return None
		
		# reverse children sub trees first
		left = root.left
		right = root.right
		
		# swap left and right children
		root.left = self.invertTree(right)
		root.right = self.invertTree(left)
		
		# return root with reverted children
		return root