# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
		
class BSTIterator:
	# @param root, a binary search tree's root node
	def __init__(self, root):
		self.current = root
		self.stack = []
		
	# @return a boolean, whether we have a next smallest number
	def hasNext(self):
		return self.current or self.stack

	# @return an integer, the next smallest number
	def next(self):
		#move to the left most child
		while self.current:
			self.stack.append(self.current)
			self.current = self.current.left
		
		#retreive smallest element then switch to left
		self.current = self.stack.pop(-1)
		value = self.current.val
		self.current = self.current.right
		return value





a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

c.left = b
c.right = d
b.left = a
d.right = e

# Your BSTIterator will be called like this:
i, v = BSTIterator(c), []
while i.hasNext(): v.append(i.next())
print v
