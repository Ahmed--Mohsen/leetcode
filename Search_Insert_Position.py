class Solution:
	# @param A, a list of integers
	# @param target, an integer to be inserted
	# @return integer
	def searchInsert(self, A, target):
		if len(A) == 0:
			return 0
		
		start = 0
		end = len(A) - 1
		
		while start <= end:
			mid = (start + end) / 2
			if A[mid] == target:
				return mid #target found
			if A[mid] > target:
				end = mid - 1
			else: #A[mid] < target
				start = mid + 1

		#target not found
		return start


s = Solution()
print s.searchInsert([1], 2)
			
			