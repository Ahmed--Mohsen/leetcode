"""

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

"""

############################## one stack Solution ##############################
class Solution:
	
	# @param height, a list of integer
	# @return an integer
	def largestRectangleArea(self, height):
		n = len(height)
		
		# base case
		if n == 0: return 0
		
		stack = []
		i = 0
		area = 0
		
		while i < n:
			# the peek of the stack is smaller than current hist[i]
			if len(stack) == 0 or height[stack[-1]] <= height[i]:
				stack.append(i)
				i += 1
			# height[i] is smaller than peek ... calc current area with peek as height
			else:
				tp = stack.pop(-1)
				width = i if len(stack) == 0 else i - stack[-1] - 1
				area = max(area, height[tp] * width)
		
		# remaining heights
		while stack:
			tp = stack.pop(-1)
			width = i if len(stack) == 0 else i - stack[-1] - 1
			area = max(area, height[tp] * width)
			
		return area
		
		

############################## Another Solution ##############################
class Solution:
	
	# @param height, a list of integer
	# @return an integer
	def largestRectangleArea(self, height):
		n = len(height)
		
		# base case
		if n == 0: return 0
		
		left = []
		right = []
		
		# will hold the max width for height[i] (when its the smallest)
		width = [1] * n 

		# check bars on the left of height[i]
		for i in range(n):
			while len(left) > 0 and height[i] <= height[left[-1]]:
				left.pop() # the peek can participate in width[i]
				
			# all left bars are taller that height[i]
			if len(left) == 0: 
				width[i] += i 
			
			# peek would be the barrier from left
			else:
				width[i] += i - (left[-1] + 1) 
			
			left.append(i)

		#check bars on the right of height[i]
		for i in range(n-1, -1, -1) :
			while len(right) > 0 and height[i] <= height[right[-1]]:
				right.pop() # the peek can particioate in width[i]
			
			# all right bars are taller that height[i]
			if len(right) == 0: 
				width[i] += (n - 1) - i # from n-1 (last bar) to i 
			
			# peek would be the barrier from right
			else:
				width[i] += (right[-1] - 1) - i 
			
			right.append(i)
			
		# get max area
		max_area = -1
		for i in range(n):
			max_area = max(max_area, width[i]*height[i])
		return max_area
			
#s = Solution()
#print s.largestRectangleArea([2,4])