"""

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


Note:
Your solution should be in logarithmic complexity.

"""

class Solution:
	
	# @param num, a list of integer
	# @return an integer
	def findPeakElement(self, num):
		start = 0
		end = len(num) - 1
		
		while start < end:
			mid1 = (start + end) / 2
			mid2 = mid1 + 1
			
			# peak is after the mid1
			if num[mid1] < num[mid2]: 
				start = mid2
			
			# peak exist before the mid1
			else: 
				end = mid1
				
		return start