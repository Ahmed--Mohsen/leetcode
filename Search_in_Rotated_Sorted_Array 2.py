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
			mid = (start+end)/2
			if A[mid] == target:
				return True
			if A[start] < A[mid]: #left half is sorted
				if A[start] <= target and target < A[mid]: #target in left half
					end = mid - 1
				else: #target in right half
					start = mid + 1
			elif A[mid] < A[end]: #right half is sorted
				if A[mid] < target and target <= A[end]: #target in right half
					start = mid + 1
				else: #target in left half
					end = mid - 1
			else: #duplication occured move one step
				if A[start] == target:
					return True
				if A[end] == target:
					return True
				start += 1
				end -= 1
				
		return False	
		
s = Solution()
print s.search([1,1,1,3], 2)