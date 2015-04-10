# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	
	def __str__(self):
		return str(self.val)
	

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderBottom(self, root):
		if root == None:
			return []
			
		level = 0
		queue = [] # will carry nodes in the same level
		
		queue.append(root)
		result = []
		
		while len(queue) > 0:
			level_len = len(queue)
			level = []
			for i in range(level_len):
				node = queue.pop(0)
				level.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			result.insert(0, level) #the only difference

		return result
			
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderOld(self, root):
		if root == None:
			return []
			
		level = 0
		queue = [] # will carry nodes to be visited plus there level
		
		queue.append(root)
		queue.append(0)
		result = []
		
		while len(queue) > 0:
			current_node = queue.pop(0)
			current_level = queue.pop(0)
			
			#add current node to result
			if len(result) <=  current_level:
				result.append([current_node.val])
			else:
				result[current_level].append(current_node.val)

			#visit children
			if current_node.left:
				queue.append(current_node.left)
				queue.append(current_level + 1)
			if current_node.right:
				queue.append(current_node.right)
				queue.append(current_level + 1)

		return result
	
	def print_queue(self, queue):
		for node in queue:
			print node,
		print "\n"
	

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)

root_right = TreeNode(20)
root.right = root_right
root_right.left = TreeNode(15)
root_right.right = TreeNode(7)

print s.levelOrderBottom(root)
			