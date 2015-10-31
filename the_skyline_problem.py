LEFT = 0; RIGHT = 1; HIEGHT = 2
	
class Solution(object):


	"""
	:type buildings: List[List[int]]
	:rtype: List[List[int]]
	"""
	def getSkyline(self, buildings):
		n = len(buildings)
		
		if n == 0:
			return []
			
		return self.getSkylineHelper(buildings, 0, n-1)
	
	def getSkylineHelper(self, buildings, low, high):
		result = []
		
		# base case ... One building
		if low == high:
			building = buildings[low]
			result.append([building[LEFT], building[HIEGHT]])
			result.append([building[RIGHT], 0])
			return result
		
		# split building into 2 halfs 
		mid = low + ((high-low) >> 1)
		left = self.getSkylineHelper(buildings, low, mid)
		right = self.getSkylineHelper(buildings, mid+1, high)
		
		# merge left and right to get final answer
		return self.mergeSkylines(left, right)
		
	
	def mergeSkylines(self, left, right):
		i, j = 0, 0
		left_max, right_max = 0, 0
		max_height = 0
		result = []

		while i < len(left) and j < len(right):
			curr_left, curr_right = left[i], right[j]
			x = 0; h = 0
			
			# compare x coordinate
			if curr_left[0] < curr_right[0]:
				x = curr_left[0]
				left_max = curr_left[1]
				i += 1
			
			elif curr_left[0] > curr_right[0]:
				x = curr_right[0]
				right_max = curr_right[1]
				j += 1
			
			else:
				x = curr_left[0]
				left_max = curr_left[1]
				right_max = curr_right[1]
				i += 1
				j += 1

			# compare heights	
			h = max(left_max, right_max)
			
			# check for duplicates
			if len(result) == 0 or h != result[-1][1]:
				result.append([x, h])
		
		# add remaining left or right
		while i < len(left):
			result.append(left[i])
			i += 1
		
		while j < len(right):
			result.append(right[j])
			j += 1
		
		return result



######################## Non Accepted Solution ########################
	
	"""
	:type buildings: List[List[int]]
	:rtype: List[List[int]]
	"""
	def getSkylineNaive(self, buildings):
		n = len(buildings)
		
		if n == 0:
			return 0
			
		li = 0; ri = 1; hi = 2
		min_x = buildings[0][li]
		max_x = buildings[-1][ri]
		heights = [0] * (max_x - min_x + 1)
		
		for building in buildings:
			height = building[hi]
			for x in range(building[li], building[ri]+1):
				heights[x - min_x] = max(heights[x - min_x], height)
		
		# calc key points
		key_points = [[min_x, heights[0]]]
		for i in range(1, len(heights)):
			
			# moved down
			if heights[i] < heights[i-1]:
				key_points.append([i-1+min_x, heights[i]])
			
			# moved up
			elif heights[i] > heights[i-1]:
				key_points.append([i+min_x, heights[i]])
		
		key_points.append([max_x, 0])
		
		return key_points


s = Solution()
#print s.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
print s.getSkyline([ [1,4,2], [3,5,4] ])
				
		
		