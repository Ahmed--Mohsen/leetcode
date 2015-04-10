class Solution:
	# @param num, a list of integer
	# @return an integer
	def findPeakElement(self, num):
		start = 0
		end = len(num) - 1
		
		while start < end:
			mid = (start + end) / 2
			post_mid = mid + 1
			
			if num[mid] < num[post_mid]: #peak is after the mid
				start = post_mid
			else: #peak exist before the mid
				end = mid
				
		return start