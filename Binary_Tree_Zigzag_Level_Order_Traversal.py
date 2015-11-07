"""

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

from collections import deque

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
			
		queue = deque([root])
		direction = True
		result = []
		
		while(len(queue) > 0):
			
			current_level_size = len(queue)
			current_level = deque([])
			
			for i in range(current_level_size):
				current_node = queue.popleft()
				
				#add current node children to be visited
				if current_node.left:
					queue.append(current_node.left)
				if current_node.right:
					queue.append(current_node.right)
				
				#add visited ndoes in zigzag style
				if direction == True: # from left to right
					current_level.append(current_node.val)
				else: # from right to left
					current_level.appendleft(current_node.val)
			
			#save current level
			result.append(list(current_level))
			
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
