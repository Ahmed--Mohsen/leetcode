class Solution:
  # @param a list of integers
  # @return an integer
	def removeDuplicates(self, A):
		if len(A) <= 1:
			return len(A)		
		count = 1
		for i in range(1, len(A)):
			if A[i] != A[i-1]:
				A[count] = A[i]
				count += 1
		return count
		
		
s = Solution()
print s.removeDuplicates([1,1,2])