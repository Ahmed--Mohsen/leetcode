# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a boolean
	def pathSum(self, root, sum):
		if root == None:
			return False
		self.paths = []
		self.hasPathSumHelper(root, sum, [])
		return self.paths
	
	def hasPathSumHelper(self, root, sum, path):
		if root == None:
			return
		
		#visit root
		sum -= root.val
		path.append(root.val)
		if root.left == None and root.right == None and sum == 0:
			self.paths.append(list(path))
		
		#visit children
		if root.left:
			self.hasPathSumHelper(root.left, sum, path)
		if root.right:
			self.hasPathSumHelper(root.right, sum, path)
		path.pop()
			
		
s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(1)
t.right.left = TreeNode(1)
print s.pathSum(t,3)
