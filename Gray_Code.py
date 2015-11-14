"""

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

"""

class Solution:
	
	# @return a list of integers
	# O(n)
	def grayCode(self, n):
		sequnece = []
		for i in range(1<<n):
			sequnece.append(i ^ i>>1) # from wikipendia
		return sequnece
		
	
	# @return a list of integers
	# iterative
	def grayCode2(self, n): 
		sequnece = [0]
		for i in range(n):
			inc = 1 << i
			for j in range(len(sequnece)-1, -1, -1):
				sequnece.append(sequnece[j]+inc)
		return sequnece
		
		
	# recursive
	def grayCode3(self, n): 
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
			