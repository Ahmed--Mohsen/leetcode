"""

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

"""

class Solution:
	
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		a = m - 1 
		b = n - 1
		i = m + n - 1
		
		while b >= 0:
			if a >= 0 and A[a] >= B[b]:
				A[i] = A[a]
				a -= 1
			else:
				A[i] = B[b]
				b -= 1
			i -= 1
			

s = Solution()
a = [2,0]
b = [1]
s.merge(a,1,b,len(b))
print a