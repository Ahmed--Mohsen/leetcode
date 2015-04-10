class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return an integer
	def search(self, A, target):
		if A == None:
			return -1
		
		return self.search_helper(A, target, 0, len(A) - 1)
		
	
	def search_helper(self, A, target, start, end):
		if start > end:
			return -1
		
		mid = (start+end)/2
		if A[mid] == target:
			return mid
		
		if A[start] <= A[mid]: #left half is sorted
			if A[start] <= target and target <= A[mid]: #target in left half
				end = mid - 1
			else: #target in right half
				start = mid + 1
		else: #right half is sorted
			if A[mid] <= target and target <= A[end]: #target in right half
				start = mid + 1
			else: #target in left half
				end = mid - 1
				
		return self.search_helper(A, target, start, end)		
		
s = Solution()
print s.search([4, 5, 6, 7, 0, 1, 2], 2)