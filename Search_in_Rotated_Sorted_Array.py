"""

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return an integer
	def search(self, A, target):
		# base case
		if A == None: return -1
		
		# rotated binary search
		start = 0
		end = len(A) - 1
		
		while start <= end:
			mid = (start + end) / 2
			
			# target found
			if A[mid] == target: return mid
		
			# left half is sorted
			if A[start] <= A[mid]: 
				
				# target in left half
				if A[start] <= target <= A[mid]: 
					end = mid - 1
					
				# target in right half
				else: 
					start = mid + 1
					
			# right half is sorted
			else: 
				
				# target in right half
				if A[mid] <= target <= A[end]: 
					start = mid + 1
					
				# target in left half
				else: 
					end = mid - 1
		
		# not found
		return -1
		
		
s = Solution()
print s.search([4, 5, 6, 7, 0, 1, 2], 2)