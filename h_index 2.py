"""

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

"""

class Solution(object):
	
	"""
	:type citations: List[int]
	:rtype: int
	"""
	def hIndex(self, citations):
		n = len(citations)
		
		# base case
		if n == 0: return 0
		
		low = 0
		high = n-1
		
		while low <= high:
			mid = low + ( (high - low) >> 1)
			
			# means there are citations[mid] papers that have at least citations[mid] citations.
			if citations[mid] == n - mid:
				return n - mid
			
			# means there are citations[mid] papers that have more than citations[mid] citations
			elif citations[mid] > n - mid:
				high = mid - 1
			
			# means there are citations[mid] papers that have less than citations[mid] citations
			else:
				low = mid + 1
		
		return n - low


s = Solution()
print s.hIndex([1])