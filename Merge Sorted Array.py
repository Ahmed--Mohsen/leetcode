class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		a = m -1 
		b = n - 1
		i = m+n-1
		while b >= 0:
			if a >= 0 and A[a] >= B[b]:
				A[i] = A[a]
				a -= 1
			else:
				A[i] = B[b]
				b -= 1
			i -= 1
			

s = Solution()
#a = [1,2,3,-1,-1,-1,-1,-1,-1,-1]
#b = [4,5,6,7,8,9]
a = [2,0]
b = [1]
s.merge(a,1,b,len(b))
print a