import random

class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {integer}
	def findKthLargest(self, nums, k):
		n = len(nums)
		
		# base case
		if n == 0:
			return 0
		
		# convert k to smallest index ... index starting from zero
		k = n - k
		return self.findKthLargestHelper(nums, k, 0, n - 1)
	
	
	def findKthLargestHelper(self, nums, k, left, right):
		# nums contains one element
		if left == right:
			return nums[left]
			
		# choose pivot indx between left and right
		pivot_index = random.randint(left, right)

		# find the sorted order of pivot
		pivot_index = self.partition(nums, left, right, pivot_index)

		# found the kth element
		if pivot_index == k:
			return nums[pivot_index]
		
		# search in the left to the pivot
		elif pivot_index > k:
			return self.findKthLargestHelper(nums, k, left, pivot_index - 1)
			
		# search in the right to the pivot
		else: # pivot_index < k
			return self.findKthLargestHelper(nums, k, pivot_index + 1, right)
		
	
	# @param {integer[]} nums
	# @param {integer} left
	# @param {integer} right
	# @param {integer} pivot_index
	def partition(self, nums, left, right, pivot_index):
		# store pivot value
		pivot = nums[pivot_index]

		# move pivot to the end
		self.swap(nums, pivot_index, right)
		
		#swap all element smaller than pivot to the left
		store_index = left
		for i in range(left, right):
			if nums[i] < pivot:
				self.swap(nums, i, store_index)
				store_index += 1
		
		# move pivot to its sorted place
		self.swap(nums, store_index, right)		

		# return the sorted index of the pivot
		return store_index
	
	
	def swap(self, array, i, j):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
		

s = Solution()
print s.findKthLargest([3,6,7,4,1,2,9], 3)
#print s.partition([3,6,7,4,1,2,9], 0, 6, 3)
