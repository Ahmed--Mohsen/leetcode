class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):		
		m = len(A); n = len(B)
		if (m+n)%2 == 0: #even merged ... take average of middle elements
			return ( self.get_at_k(A, B, (m+n)/2) + self.get_at_k(A, B, (m+n)/2 + 1) ) / 2.0
		else: #odd take the middle
			return self.get_at_k(A, B,(m+n)/2 + 1)
		
	#gets the element at position k in the merged array A nad B
	def get_at_k(self, A, B, k):
		m = len(A); n = len(B)
		
		if m == 0: #the kth element is in place inside b
			return B[k-1]
		if n == 0: #the kth element is in place inside a
			return A[k-1]
		
		if k == 1: #kth element is the first in either
			return min(A[0], B[0])
		
		i = min(m, k/2)
		j = min(n, k/2)
		if A[i-1] > B[j-1]: #increase B median
			return self.get_at_k(A[:k-j], B[j:], k - j)
		else: # increase A median
			return self.get_at_k(A[i:], B[:k-i], k - i)
		return 0



s = Solution()
print s.findMedianSortedArrays([1], [2,3,4,5,6,7,8])