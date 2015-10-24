class Solution:
  # @param a list of integers
  # @return an integer
	def removeDuplicates(self, A):
		# base case
		if len(A) <= 1:
			return len(A)		
		
		# the position of last uniqe element
		index = 0
		
		# make sure only unique elements are before index
		for i in range(1, len(A)):

			# no duplicates for A[index]
			if A[index] != A[i]:
				index += 1
				A[index] = A[i]
		
		return index + 1
			
s = Solution()
print s.removeDuplicates([1,1])