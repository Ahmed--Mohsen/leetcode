# -*- coding: utf-8 -*-
"""

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

"""

class SegmentTreeNode(object):
	"""
	node for SegmentTree
	"""
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.left = None
		self.right = None
		self.sum = 0

class SegmentTree(object):
	"""
	Segment Tree implementation
	query = O(logn)
	update = O(logn)
	"""
	def __init__(self, nums): 
		self.root = self.build(nums, 0, len(nums) - 1)
		
		
	def build(self, nums, start, end):
		# base case
		if start > end:
			return None
		
		root = SegmentTreeNode(start, end)
		
		# single value vase
		if start == end:
			root.sum = nums[start]
			
		# build left and right subtrees recusively
		else:
			mid = start + ((end - start) >> 1)
			root.left = self.build(nums, start, mid)
			root.right = self.build(nums, mid + 1, end)
			root.sum = root.left.sum + root.right.sum
		
		return root
		
	
	"""
	wrapper of update
	"""
	def update(self, pos, val):
		self._update(self.root, pos, val)
	
	"""
	concrete impl. of update
	"""
	def _update(self, root, pos, val):
		# found node
		if root.start == root.end:
			root.sum = val
			
		# update the path from root till leave having pos
		else:
			mid = root.start + ((root.end - root.start) >> 1)
			if pos <= mid:
				self._update(root.left, pos, val)
			else:
				self._update(root.right, pos, val)
			
			# update parent
			root.sum = root.left.sum + root.right.sum
	
	
	"""
	wrapper of query
	"""				
	def query(self, start, end):
		return self._query(self.root, start, end)
		
			
	"""
	concrete impl. of query
	"""				
	def _query(self, root, start, end):
		# found node
		if root.start == root.end:
			return root.sum
		
		# search in children
		mid = root.start + ((root.end - root.start) >> 1)
		
		# all query in left child
		if end <= mid:
			return self._query(root.left, start, end)
		
		# all quert in right child
		elif start >= mid+1:
			return self._query(root.right, start, end)
		
		# root both children has queries
		else:
			return self._query(root.left, start, mid) + self._query(root.right, mid+1, end)
			
			

class NumArray(object):
	
	"""
	initialize your data structure here.
	:type nums: List[int]
	"""
	def __init__(self, nums):
		self.tree = SegmentTree(nums)
		
	
	"""
	:type i: int
	:type val: int
	:rtype: void
	"""	
	def update(self, i, val):
		self.tree.update(i, val)
		

	"""
	sum of elements nums[i..j], inclusive.
	:type i: int
	:type j: int
	:rtype: int
	"""
	def sumRange(self, i, j):
		return self.tree.query(i, j)


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 3, 5])
print numArray.sumRange(0, 2)
numArray.update(1, 2)
print numArray.sumRange(0, 2)