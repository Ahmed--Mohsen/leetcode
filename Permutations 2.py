"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

"""

class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		# base case
		if num == None or len(num) <= 1:
			return [num]
			
		num.sort()
		self.result = []
		self.permute_helper(num, 0)
		return self.result
		
	def permute_helper(self, num, index):
		# base case
		if index == len(num) - 1: 
				self.result.append(list(num))
		else:
			for i in range(index, len(num)):
				if self.has_no_duplicates(num, index, i):
					self.swap(num, index, i)
					self.permute_helper(num, index+1) # recurse
					self.swap(num, index, i) # backtrack

	def swap(self,num, i, j):
		temp = num[i]
		num[i] = num[j]
		num[j] = temp
		
	def has_no_duplicates(self, num, start, end):
		for i in range(start,end):
			if num[i] == num[end]:
				return False
		return True
		
s = Solution()
print s.permuteUnique([1,1,2])