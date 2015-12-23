"""

There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

"""

class Solution:
	
	# @return a float
	def findMedianSortedArrays(self, A, B):		
		m = len(A); n = len(B)
		
		# even merged ... take average of middle elements
		if (m + n) % 2 == 0: 
			return ( self.get_at_k(A, B, (m + n) / 2) + self.get_at_k(A, B, (m + n) / 2 + 1) ) / 2.0
			
		# odd take the middle
		else: 
			return self.get_at_k(A, B, (m + n) / 2 + 1)

		
	#gets the element at position k in the merged array A nad B
	def get_at_k(self, A, B, k):
		m = len(A); n = len(B)
		
		# the kth element is in place inside b
		if m == 0: 
			return B[k-1]
			
		# the kth element is in place inside a
		if n == 0: 
			return A[k-1]
		
		# kth element is the first in either
		if k == 1: 
			return min(A[0], B[0])
		
		i = min(m, k / 2)
		j = min(n, k / 2)
		
		# increase B median
		if A[i-1] > B[j-1]: 
			return self.get_at_k(A[:k-j], B[j:], k - j)
			
		# increase A median
		else: 
			return self.get_at_k(A[i:], B[:k-i], k - i)
		return 0



s = Solution()
print s.findMedianSortedArrays([1], [2,3,4,5,6,7,8])