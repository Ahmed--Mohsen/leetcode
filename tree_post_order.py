"""

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

"""

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	
	def __init__(self):
		self.path = []

	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		self.traverse(root)
		return self.path

	def traverse(self, root):
		if root == None:
			return
			
		if root.left != None:
			self.postorderTraversal(root.left)
		
		if root.right != None:
			self.postorderTraversal(root.right)
			
		#visit root
		self.path.append(root.val)

"""
s = Solution()
t = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t.right = t2
t2.right = t3
print s.postorderTraversal(t)
"""