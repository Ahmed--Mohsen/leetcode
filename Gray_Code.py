class Solution:
	# @return a list of integers
	def grayCode2(self, n): #iterative
		sequnece = [0]
		for i in range(n):
			inc = 1 << i
			for j in range(len(sequnece)-1, -1, -1):
				sequnece.append(sequnece[j]+inc)
		return sequnece
		
	def grayCode(self, n): #recursive
		if n == 0:
			return [0]
		
		prev = self.grayCode(n-1)
		inc = 1 << n-1
		for i in range(len(prev)-1, -1, -1):
			prev.append(prev[i]+inc)
		return prev
			
		


s = Solution()
print s.grayCode2(3)
print s.grayCode(3)
			