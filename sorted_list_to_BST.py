# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param num, a list of integers
	# @return a tree node
	def sortedArrayToBST(self, num):
		if num == None or len(num) == 0:
			return None
		
		return self.sortedArrayToBSTHelper(num, 0, len(num) - 1)
	
	def sortedArrayToBSTHelper(self, num, low, high):
		#base case
		if low > high:
			return None
		mid = (low+high)/2
		root = TreeNode(num[mid])
		root.left = self.sortedArrayToBSTHelper(num, low, mid - 1)
		root.right = self.sortedArrayToBSTHelper(num, mid + 1, high)
		return root