# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
	
	"""
	:type n: int
	:rtype: int
	"""
	def firstBadVersion(self, n):
		left = 1
		right = n
		
		# perform binary search
		while left < right:
			mid = left + (right - left) / 2
			if isBadVersion(mid):
				right = mid
			else:
				left = mid + 1
		
		# first ever bad
		return left