"""

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""

class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return a list of length 2, [index1, index2]
	def searchRange(self, A, target):
		n = len(A)
		result = [-1, -1]
		
		# base case
		if n == 0: return result
		
		# search for target
		left = self.first_occurance(A, target)
		
		# element is present
		if left < n and A[left] == target: 
			right = self.first_occurance(A, target + 1)
			return [left, right - 1]
			
		# no occurance occured
		else: 
			return [-1 , -1]
			
	
	# return the index of the first element to be equal to target
	# same as lower bound or found insert position
	def first_occurance(self, A, target):
		start = 0
		end = len(A) - 1
		while start <= end:
			mid = ( start + end ) / 2
			if A[mid] < target:
				start = mid + 1
			else:
				end = mid - 1
		return start
		

s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 8)