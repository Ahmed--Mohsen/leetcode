"""

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

class Solution:
	
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSumClosest(self, num, target):
		
		# base case
		if len(num) < 3:
			return sum(num)
		
		num.sort()
		close = num[0] + num[1] + num[2]
		
		for i in range(len(num) - 2):
			start = i + 1
			end = len(num) - 1
			
			while start < end:
				close_sum = num[i] + num[start] + num[end]
				
				# found exact match
				if close_sum == target: 
					return target
					
				if abs(target - close_sum) < abs(target - close):
					close = close_sum
					
				# search for smaller
				if close_sum > target:  
					end -= 1
				else:
					start += 1
		return close
	

s = Solution()				
print s.threeSumClosest([0,0,0], 1)
		