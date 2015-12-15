# -*- coding: utf-8 -*-
"""

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

class Solution:
	
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	def nextPermutation(self, num):
		n = len(num)
		
		if n <= 1:
			return
		
		# traverse backward to find the first one with index i that satisfy num[i-1] < num[i]
		i = n - 1
		while i > 0 and num[i-1] >= num[i]: # decreasing order
			i -= 1
		
		if i <= 0:
			num.sort()
			return
			
		 # Find successor to pivot
		j = n - 1 
		while num[j] <= num[i-1]:
			j -= 1
		
		self.swap(num, i-1, j)

		# Reverse suffix
		j = n - 1
		while j > i:
			self.swap(num, i, j)
			i += 1
			j -= 1


	def swap(self, num, i, j):
		temp = num[i]
		num[i] = num[j]
		num[j] = temp
		


s = Solution()
p = [3,2,1]
s.nextPermutation(p)
print p