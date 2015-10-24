class Solution(object):
	
	"""
	:type num: int
	:rtype: int
	"""
	def nthUglyNumber(self, n):
		# base case
		if n < 1:
			return 1
		
		# 1 is the first ever ugly number
		ugly = [1]
		
		# treat each multiplies of the factors (2, 3, 5)
		# as a sorted list that needed to be merged
		p2 = 0; p3 = 0; p5 = 0
		
		for i in range(1, n):
			
			# calc next ugly number
			next_ugly = min(2 * ugly[p2], 3 * ugly[p3], 5 * ugly[p5])
			ugly.append(next_ugly)
			
			# decide which pointer to be incremented (after merge)
			if next_ugly == 2 * ugly[p2]: p2 += 1
			if next_ugly == 3 * ugly[p3]: p3 += 1		
			if next_ugly == 5 * ugly[p5]: p5 += 1
			
		return ugly[-1]