class Solution:
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		if A == None or len(A) == 0:
			return 0
		i = 0
		j = len(A) - 1
		while i <= j:
			if A[i] == elem:
				#search for element to swap with
				while j > i and A[j] == elem:
					j -= 1
				self.swap(A,i,j)
			i += 1
		return j if A[j] == elem else j + 1
			
	def swap(self,A, i, j):
		temp = A[i]
		A[i] = A[j]
		A[j] = temp
		
s = Solution()
print s.removeElement([2], 6)