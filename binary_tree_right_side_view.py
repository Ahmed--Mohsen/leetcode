# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[]}
	# iterative solution
	def rightSideView(self, root):
		# base case
		if root == None:
			return []

		# BFS queue
		queue = [root]
	
		# result list
		side_view = []
	
		while queue:
			# extract the right most element in the order
			# level traversal
			current = queue[-1]
			side_view.append(current.val)
		
			# visit all node in cuurent level
			level_len = len(queue)
			for i in range(level_len):
				node = queue.pop(0)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
	
		return side_view
		
		
	# @param {TreeNode} root
	# @return {integer[]}
	# recursive solution
	def rightSideViewRecursive(self, root):
		# base case
		if root == None:
			return []

		result = []
		self.traverse(root, 1, result)
		return result
	
	def traverse(self, root, level, res):
		# stopping creteria
		if root == None: return
		
		# means current node is the first to be seen
		# in this level from the right
		if level > len(res):
			res.append(root.val)
		
		# visit children
		if root.right:
			self.traverse(root.right, level+1, res)
		if root.left:
			self.traverse(root.left, level+1, res)
			


s = Solution()
#print s.rightSideView(TreeNode(1))
print s.rightSideViewRecursive(TreeNode(1))
