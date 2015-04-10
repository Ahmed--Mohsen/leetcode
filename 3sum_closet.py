class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSumClosest(self, num, target):
		#base case
		if len(num) < 3:
			return sum(num)
		
		num.sort()
		close = num[0] + num[1] + num[2]
		
		for i in range(len(num) - 2):
			start = i + 1
			end = len(num) - 1
			while start < end:
				close_sum = num[i] + num[start] + num[end]
				
				if close_sum == target: #found exact match
					return target
					
				if abs(target - close_sum) < abs(target - close):
					close = close_sum
				if close_sum > target:  #search for smaller
					end -= 1
				else:
					start += 1
		return close
	

s = Solution()				
print s.threeSumClosest([0,0,0], 1)
		