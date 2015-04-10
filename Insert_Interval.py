# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	
	def __str__(self):
		return "("+str(self.start)+","+str(self.end)+")"

class Solution:
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		stack = [newInterval]
		
		#try insert new interval first
		for i in range(len(intervals)):
			current = stack[-1]
			next = intervals[i]
			
			if next.end < current.start: #insert below
				stack.pop()
				stack.append(next)
				stack.append(current)
			elif next.start > current.end: #insert above
				stack.append(next)
			else: #merge
				current.start = min(current.start, next.start)
				current.end = max(current.end, next.end)
				
		return stack
				
		
s = Solution()
intervals = [Interval(1, 5)]
newInterval = Interval(0,3)

x = s.insert(intervals, newInterval)
for y in x:
	print y,