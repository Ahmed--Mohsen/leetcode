"""

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

"""

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
print s.removeDuplicates([1,1,2,2,2,3])