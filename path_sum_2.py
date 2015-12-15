"""

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""

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
		self.paths = []
		self.hasPathSumHelper(root, sum, [])
		return self.paths
	
	def hasPathSumHelper(self, root, sum, path):
		# base case
		if root == None: return
		
		# visit root
		path.append(root.val)
		
		# check end of leave nodes
		if root.left == None and root.right == None and sum == root.val:
			self.paths.append(list(path))
		
		# visit children
		else:
			if root.left: self.hasPathSumHelper(root.left, sum - root.val, path)
			if root.right: self.hasPathSumHelper(root.right, sum - root.val, path)
			
		# backtrack
		path.pop()
			
		
s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(1)
t.right.left = TreeNode(1)
print s.pathSum(t,3)
