"""

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

"""

# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	
	def __repr__(self):
		return "("+str(self.start)+","+str(self.end)+")"
		
		
class Solution:
	
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		start = newInterval.start
		end = newInterval.end
		
		# keep track for intervals before and after newInterval
		left = []
		right = []
		
		for interval in intervals:
			
			# before new interval
			if start > interval.end:
				left += [interval]
		
			# after new interval
			elif end < interval.start:
				right += [interval]
			
			# merge
			else:
				start = min(start, interval.start)
				end = max(end, interval.end)
				
		return left + [Interval(start, end)] + right
		
############################### Another Solution ###############################
"""
class Solution:
	
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		stack = [newInterval]
		
		# try insert new interval first
		for i in range(len(intervals)):
			current = stack[-1]
			next = intervals[i]
			
			if next.end < current.start: # insert below
				stack.pop()
				stack.append(next)
				stack.append(current)
			elif next.start > current.end: # insert above
				stack.append(next)
			else: # merge
				current.start = min(current.start, next.start)
				current.end = max(current.end, next.end)
				
		return stack
				
"""
s = Solution()
intervals = [Interval(1, 5)]
newInterval = Interval(6,8)

print s.insert(intervals, newInterval)
