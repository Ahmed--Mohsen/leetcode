"""

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

"""

class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return an integer
	def search(self, A, target):
		if A == None:
			return False
		
		start = 0
		end = len(A) - 1
		
		while (start <= end):
			mid = (start + end) / 2
			
			# found
			if A[mid] == target: return True
			
			# left half is sorted
			if A[mid] > A[start]: 
				
				# target in left half
				if A[start] <= target < A[mid]: 
					end = mid - 1
					
				# target in right half
				else: 
					start = mid + 1
					
			# right half is sorted
			elif A[mid] < A[start]:
				
				# target in right half
				if A[mid] < target <= A[end]: 
					start = mid + 1
					
				# target in left half
				else: 
					end = mid - 1
					
			# duplication occured move one step
			else:
				start += 1
		
		# not found
		return False
		
s = Solution()
print s.search([1,1,1,3], 1)