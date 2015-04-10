# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @return a list of tree node
	def generateTrees(self, n):
		return self.generateTreesHelper(1, n)


	def generateTreesHelper(self, start, end):
		trees = []
		if start > end: #incase of no left or right child
			trees.append(None)
		else:
			for i in range(start, end+1):
				lefts = self.generateTreesHelper(start, i-1)
				rights = self.generateTreesHelper(i+1, end)
				for left in lefts:
					for right in rights:
						root = TreeNode(i)
						root.left = left
						root.right = right
						trees.append(root)
		return trees

s = Solution()
x = s.generateTrees(3)
for i in range(len(x)):
	print x[i].val