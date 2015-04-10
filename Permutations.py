class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permute(self, num):
		if num == None or len(num) <= 1:
			return [num]
		num.sort()
		self.result = []
		self.permute_helper(num, 0)
		return self.result
		
	def permute_helper(self, num, index):
		if index == len(num) - 1: #base case
			self.result.append(list(num))
		else:
			for i in range(index, len(num)):

				self.swap(num, index, i)
				self.permute_helper(num, index+1) #recurse
				self.swap(num, index, i) #backtrack

	def swap(self,num, i, j):
		temp = num[i]
		num[i] = num[j]
		num[j] = temp
		

s = Solution()
print s.permute([1,2,3])