class Solution:
  # @param a list of integers
  # @return an integer
	def removeDuplicates(self, A):
		if len(A) <= 2:
			return len(A)		
		count = 2
		pointer = 2
		while pointer < len(A) :
			if A[pointer] != A[count - 2]:
				A[count] = A[pointer]
				count += 1
			pointer += 1
		return count
			
s = Solution()
print s.removeDuplicates([1,1,1,2])