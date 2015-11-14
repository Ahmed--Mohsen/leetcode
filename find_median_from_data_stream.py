"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2

"""

import heapq

class MedianFinder:
	
	"""
	Initialize your data structure here.
	"""
	def __init__(self):
		# max heap (add elements multiplied by -1 to
		# make min heap act as max heap) 
		self.left_heap = []
		
		# min heap
		self.right_heap = []

	"""
	Adds a num into the data structure.
	:type num: int
	:rtype: void
	"""
	def addNum(self, num):
		# add first to max heap
		heapq.heappush(self.left_heap, -num)
		
		# rebalance the inner elements
		max_left = -heapq.heappop(self.left_heap)
		heapq.heappush(self.right_heap, max_left)
		
		# check the sizes
		if len(self.left_heap) < len(self.right_heap):
			min_right = heapq.heappop(self.right_heap)
			heapq.heappush(self.left_heap, -min_right)

	"""
	Returns the median of current data stream
	:rtype: float
	"""
	def findMedian(self):
		# odd case
		if len(self.left_heap) > len(self.right_heap):
			return -self.left_heap[0]
		
		# even case
		return (self.right_heap[0] - self.left_heap[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(3)
mf.addNum(0)

print mf.findMedian()