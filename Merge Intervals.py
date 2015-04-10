# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

def interval_cmp(self, other):
	return self.start - other.start

def interval_str(self):
	return "("+str(self.start)+", "+str(self.end)+")"
	
Interval.__cmp__ = interval_cmp
Interval.__str__ = interval_str

class Solution:
	# @param intervals, a list of Interval
	# @return a list of Interval
	def merge(self, intervals):
		if intervals == None or len(intervals) <= 1:
			return intervals
			
		intervals.sort()
		merged_intervals = [intervals[0]]
		
		for i in range(1, len(intervals)):
			current_interval = intervals[i]
			starting_interval = merged_intervals[-1]
			
			#no overlapping
			if starting_interval.end < current_interval.start:
				merged_intervals.append(current_interval)
			
			#overlap occured ... merge them
			elif starting_interval.end < current_interval.end: 
				starting_interval.end = current_interval.end
		
		return merged_intervals
			

s = Solution()
i1 = Interval(1,3)
i2 = Interval(2,6)
i3 = Interval(8,10)
s.merge([i1, i2, i3])
		
		
		