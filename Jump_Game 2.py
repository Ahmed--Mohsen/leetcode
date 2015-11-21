"""

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

"""

class Solution:
	
	# @param A, a list of integers
	# @return a boolean
	def jump(self, A):
		n = len(A)
		if n < 2:
			return 0
			
		level = 0
		i = 0
		current_max = 0
		next_max = 0

		while current_max - i + 1 > 0:  # num of nodes in current level > 0
			level += 1
			while i <= current_max:
				next_max = max(next_max, i + A[i])
				if next_max >= n - 1: # reached the end
					return level
				i += 1
			current_max = next_max
		return 0
			

s = Solution()
print s.jump([2,3,1,1,4])
		
		
		
				