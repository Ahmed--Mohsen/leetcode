"""

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""
# Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b
 
class Solution:
	
	# @param points, a list of Points
	# @return an integer
	def maxPoints(self, points):
		n = len(points)
		
		# base case
		if n < 3:
			return n
		
		# will hold the result
		max_points = 0
		
		# a line is defined as y = ax + b
		# a = (y1-y) / (x1-x)
		# for each point (x, y) keep track of all points (x1, y1)
		#  that share the same slope with the point (x, y)
		for i in range(n):
			x = points[i].x; y = points[i].y # current origin
			lines = {} # key = slope, value = points count (key = vertical for infinity slope)
			duplicates = 1 # number of points that have same coordinates (x, y)
			
			for j in range(i+1, n):
				x1 = points[j].x; y1 = points[j].y
				
				# check duplicates
				if x1 == x and y2 == y:
					duplicates += 1
				
				# check vertical points
				elif x1 == x:
					lines['vertical'] = lines.get('vertical', 0) + 1
				
				# general case: calc the slope
				else:
					slope = 1.0 * (y1 - y) / (x1 - x)
					lines[slope] = lines.get(slope, 0) + 1
			
			# calc current max for point (x, y)
			current_max = duplicates
			if lines:
				current_max += max(lines.values())
			
			# update global max
			max_points = max(max_points, current_max)
			
		return max_points	
		