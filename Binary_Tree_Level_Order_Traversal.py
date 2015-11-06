"""

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

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
	def levelOrder(self, root):
		if root == None:
			return []
			
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
			result.append(level)

		return result


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)

root_right = TreeNode(20)
root.right = root_right
root_right.left = TreeNode(15)
root_right.right = TreeNode(7)

print s.levelOrder(root)
			