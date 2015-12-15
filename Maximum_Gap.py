"""

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

"""

class Pair:
	def __init__(self, min, max):
		self.min = min
		self.max = max
		
	def __str__(self):
		return "[ min = "+str(self.min) + ", max = "+str(self.max)+" ]"

class Solution:
	# @param num, a list of integer
	# @return an integer
	def maximumGap(self, nums):
		if nums == None or len(nums) < 2: #edge case
			return 0
		
		# find max and min elements	
		n = len(nums)
		min_val = min(nums)
		max_val = max(nums)
		
		# another edge case when all array nums are equal
		if min_val == max_val:
			return 0
		
		# add nums to buckets based on the distribution	
		dist = ( ( max_val - min_val - 1) / (n - 1) ) + 1
		buckets = [ None ] * n
		for num in nums:
			b_index = (num - min_val) / dist
			pair = buckets[b_index]
			if pair == None:
				buckets[b_index] = Pair(num, num)
			else:
				pair.min = min(pair.min, num)
				pair.max = max(pair.max, num)

		# find the max gap ... max of previous - min of current (successive elements)
		max_gap = float("-inf")
		prev_bucket_max = buckets[0].max
		for i in range(1, n):
			if buckets[i]:
				max_gap = max(max_gap, buckets[i].min - prev_bucket_max)
				prev_bucket_max = buckets[i].max
		return max_gap
		
s = Solution()
print s.maximumGap([3,6,9,1])
				
		
		