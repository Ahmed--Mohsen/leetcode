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