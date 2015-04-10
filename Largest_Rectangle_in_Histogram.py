class Solution:
	# @param height, a list of integer
	# @return an integer
	def largestRectangleArea(self, height):
		n = len(height)
		if n == 0:
			return 0
		
		left = []; right = []
		width = [1]*n #will hold the max width for height[i] (when its the smallest)

		#check bars on the left of height[i]
		for i in range(n):
			while len(left) > 0 and height[i] <= height[left[-1]]:
				left.pop() #the peek can particioate in width[i]

			if len(left) == 0: #all left bars are taller that height[i]
				width[i] += i 
			else:
				width[i] += i - (left[-1] + 1) #peek would be the barrier from left
			
			left.append(i)

		#check bars on the right of height[i]
		for i in range(n-1, -1, -1) :
			while len(right) > 0 and height[i] <= height[right[-1]]:
				right.pop() #the peek can particioate in width[i]
			
			if len(right) == 0: #all right bars are taller that height[i]
				width[i] += (n - 1) - i # from n-1 (last bar) to i 
			else:
				width[i] += (right[-1] - 1) - i #peek would be the barrier from right
			
			right.append(i)
			
		#get max area
		max_area = -1
		for i in range(n):
			max_area = max(max_area, width[i]*height[i])
		return max_area
			
s = Solution()
print s.largestRectangleArea([2,4])