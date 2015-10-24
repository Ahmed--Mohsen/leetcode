class Solution(object):
	
	"""
	:type citations: List[int]
	:rtype: int
	"""
	def hIndex(self, citations):
		n = len(citations)
		count = [0] * (n+1)
		
		# base case
		if n == 0:
			return 0
		
		for c in citations:
			if c > n: # max h = n
				count[n] += 1
			else:
				count[c] += 1
		
		# move backward to take max h-index
		total = 0
		for i in range(n, 0, -1):
			total += count[i]
			if total >= i:
				return i
		
		# h-index failed
		return 0