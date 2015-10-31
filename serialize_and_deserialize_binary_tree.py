# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	
	def __repr__(self):
		return str(self.val)
		

from collections import deque

NONE = "-"
DELIMITER = ","

class Codec:
	
	"""Encodes a tree to a single string.

	:type root: TreeNode
	:rtype: str
	"""
	def serialize(self, root):
		# base case
		if root == None:
			return NONE
		
		# store the traversal order
		bfs = []
		
		# use level BFS traversal
		queue = deque([root])
		while queue:
			current = queue.popleft()
			bfs.append(current)
				
			# visit children
			if current:
				queue.append(current.left)
				queue.append(current.right)

		return DELIMITER.join([str(b.val) if b else NONE for b in bfs])


	"""Decodes your encoded data to tree.

	:type data: str
	:rtype: TreeNode
	"""
	def deserialize(self, data):
		# base case null root
		if len(data) == 1:
			return None
		
		# convert all values into tree nodes
		values = data.split(DELIMITER)
		nodes = [ TreeNode(int(value)) if value != NONE else None for value in values ]
		
		# reverse the bfs
		root = nodes[0]
		queue = deque([root])
		
		for i in range(1, len(nodes), 2):
			current = queue.popleft()
			
			# skip null nodes
			if current == None:
				continue
				
			# set current children
			current.left = nodes[i]
			current.right = nodes[i+1]
			
			# only add current children if they are not null
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)
		
		return root
		

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
#root.right = TreeNode(3)

codec = Codec()
x = codec.deserialize(codec.serialize(root))
print x, x.left, x.right