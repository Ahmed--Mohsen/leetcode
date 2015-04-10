class Solution:
	# @param num, a list of integer
	# @return a list of integer
	def nextPermutation(self, num):
		if len(num) <= 1:
			return num
		
		# Find non-increasing suffix
		i = len(num) - 1
		while i > 0 and num[i-1] >= num[i]: #decreasing order
			i -= 1
		
		if i <= 0:
			num.sort()
			return num
			
		 # Find successor to pivot
		j = len(num) - 1 
		while num[j] <= num[i-1]:
			j -= 1
		
		self.swap(num, i-1, j)

		# Reverse suffix
		j = len(num) - 1
		while j > i:
			self.swap(num, i, j)
			i += 1
			j -= 1
		
		return num


	def swap(self, num, i, j):
		temp = num[i]
		num[i] = num[j]
		num[j] = temp
		

s = Solution()
p = [3,2,1]
x = s.nextPermutation(p)
print x