class Solution:
  # @param a list of integers
  # @return an integer
	def removeDuplicates(self, A):
		# base case
		if len(A) <= 1:
			return len(A)		
		
		# the position of last uniqe element
		index = 0
		
		# the number of times duplicate occur for
		# A[index] element
		duplicated = False
		
		# make sure only unique elements are before index
		for i in range(1, len(A)):

			# check for duplication
			unique = A[index] != A[i]
			
			# only allow moving forward if the next
			# value is unique or not duplicated yet
			if unique or (not duplicated):
				index += 1
				A[index] = A[i]
				duplicated = not unique
		
		# length is 1 based and index is 0 based
		return index + 1
			
s = Solution()
print s.removeDuplicates([1,1,2])