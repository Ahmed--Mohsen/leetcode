"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		# base case
		if root == None:
			return True
			
		return self.isSymmetricHelper(root.left, root.right)
	
	
	def isSymmetricHelper(self, left, right):
		
		# both have no children
		if (left == None) and (right == None): 
			return True
			
		# one has children while other not (XOR)
		if (left == None) != (right == None): 
			return False
		
		# roots are matched checking further levels
		if left.val == right.val: 
			inner_mirror = self.isSymmetricHelper(left.right, right.left)
			outer_mirror = self.isSymmetricHelper(left.left, right.right)
			return inner_mirror & outer_mirror
		
		# roots not matched
		return False