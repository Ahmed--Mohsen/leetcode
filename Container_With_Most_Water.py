"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

"""
class Solution:
	
	# @return an integer
	def maxArea(self, height):
		n = len(height)
		low = 0
		high = n - 1
		max_area = 0
		
		while low < high:
			h = min(height[low], height[high])
			max_area = max(max_area, (high-low) * h)
			
			# move right till finding taller height
			while low < high and height[low] <= h:
				low += 1
			
			# move left till finding taller height
			while low < high and height[high] <= h:
				high -= 1
		
		return max_area