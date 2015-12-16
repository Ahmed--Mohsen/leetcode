"""

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""

class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		remaining = {}
		for i in range(len(num)):
			difference = target - num[i]
			if difference in remaining:
				j = remaining[difference]
				if i != j:
					return (j+1, i+1)
			remaining[num[i]] = i


s = Solution()
print s.twoSum([2, 7, 11, 15], 9)