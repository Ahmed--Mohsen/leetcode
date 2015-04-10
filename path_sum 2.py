# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a boolean
	def hasPathSum(self, root, sum):
		if root == None:
			return False
		return self.hasPathSumHelper(root, 0, sum)
	
	def hasPathSumHelper(self, root, current_sum, sum):
		if root == None:
			return False
		
		current_sum += root.val
		if root.left == None and root.right == None and current_sum == sum:
			return True
		
		has_left_sum = self.hasPathSumHelper(root.left, current_sum, sum)
		has_right_sum = self.hasPathSumHelper(root.right, current_sum, sum)
			
		return  has_left_sum or has_right_sum
		

s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
#t.right = TreeNode(3)
print s.hasPathSum(t,3)
