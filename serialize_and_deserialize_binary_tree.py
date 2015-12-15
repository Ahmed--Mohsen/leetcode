"""

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""

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