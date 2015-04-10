class Solution:
	# @param A a list of integers
	# @return nothing, sort in place
	def sortColors(self, A):
		if len(A) == 0:
			return
			
		red = 0; blue = 0; white = 0
		
		for i in range(len(A)):
			current = A[i]
			if current <= 2:
				A[blue] = 2
				blue += 1
			if current <= 1:
				A[white] = 1
				white += 1
			if current <= 0:
				A[red] = 0
				red += 1
				
		
s = Solution()
x = [2,1,2,1,0,0,1]
print x
s.sortColors(x)
print x