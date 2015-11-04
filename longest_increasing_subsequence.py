"""

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

"""

class Solution(object):
	
	############################## O(n log n) Solution (TLE) ##############################
	# http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
	"""
	:type nums: List[int]
	:rtype: int
	"""
	def lengthOfLIS(self, nums):
		n = len(nums)
		
		# base case
		if n < 2:
			return n
		
		# tail[i] = last number in the active sequence of len (i+1)
		# all elements in tail would be sorted by definition
		tail = [0] * n
		tail[0] = nums[0]
		
		# the length of max LIS so far
		length = 1
		
		for num in nums:

			# new smallest value
			if num < tail[0]:
				tail[0] = num
			
			# we can extend the active sequence of size len-1
			elif num > tail[length-1]:
				tail[length] = num
				length += 1
			
			# num is in between so we have to search its insert index
			# in the tail array 
			else:
				tail[self.binarySearch(nums, 0, length-1, num)] = num
		
		return length
	
	"""
	find the index of the largest number that is smaller than key
	much like finding the place of key to be inserted in order
	"""
	def binarySearch(self, nums, left, right, key):
		
		while left+1 < right:
			mid = left + ((right-left) >> 1)
			
			# move to left
			if nums[mid] >= key:
				right = mid
			
			# move to right
			else:
				left = mid + 1
		return right
				

s = Solution()
print s.lengthOfLIS([10,9,2,5,3,4])


		
class Solution(object):
		
	############################## O(n^2) Solution (TLE) ##############################
	"""
	:type nums: List[int]
	:rtype: int
	"""
	def lengthOfLIS(self, nums):
		n = len(nums)
		
		# base case
		if n < 2:
			return n
		
		# dp[i] means the len of LIS ending at index i
		# each element in nums repersent LIS of len 1
		dp = [1] * n
		max_length = 1
		
		for i in range(1, n):
			for j in range(n):
				
				# LIS can only occur if nums[j] < nums[i]
				if nums[j] < nums[i]:
					dp[i] = max(dp[i], dp[j]+1)
				
				# keep track of max dp[i]
				max_length = max(max_length, dp[i])
		
		return max_length