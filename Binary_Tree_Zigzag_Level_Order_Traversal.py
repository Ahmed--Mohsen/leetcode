# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def zigzagLevelOrder(self, root):
		if root == None:
			return []
			
		queue = [root]
		direction = True
		result = []
		while(len(queue) > 0):
			current_level_size = len(queue)
			current_level = []
			for i in range(current_level_size):
				current_node = queue.pop(0)
				
				#add current node children to be visited
				if current_node.left:
					queue.append(current_node.left)
				if current_node.right:
					queue.append(current_node.right)
				
				#add visited ndoes in zigzag style
				if direction == True: #from left to right
					current_level.append(current_node.val)
				else: #from right to left
					current_level = [current_node.val] + current_level
			
			#save current level
			result.append(current_level)
			
			#reverse direction
			direction = not direction
		
		return result

s = Solution()
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left ; root.right=right
left.right = TreeNode(4) ;  right.right = TreeNode(5)
print s.zigzagLevelOrder(root)
