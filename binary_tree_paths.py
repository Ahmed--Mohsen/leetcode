"""

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

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
	:rtype: List[str]
	"""
	def binaryTreePaths(self, root):
		result = []
		
		# base case
		if not root:
			return result
	
		self.dfs(root, [], result)
		return result
	
	def dfs(self, current, path, result):
		
		# visit current root
		path.append(current.val)
		
		# current node is a leaf node
		if  not current.left and not current.right:
			leaf_path = "->".join( str(p) for p in path )
			result.append(leaf_path)
		
		# visit children
		if current.left:
			self.dfs(current.left, path, result)
		if current.right:
			self.dfs(current.right, path, result)
		
		# backtrack from current node
		path.pop(-1)