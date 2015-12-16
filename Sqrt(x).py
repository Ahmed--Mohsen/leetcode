"""

Implement int sqrt(int x).

Compute and return the square root of x.

"""

class Solution:
	
	# @param x, an integer
	# @return an integer
	def mySqrt(self, x):
		# base case
		if x == 0: return 0
		
		# binary search for sqrt in the range 1, x
		start = 1
		end = x
		while start <= end:
			
			# calc middle and next middle
			middle = (start + end) / 2
			square = middle * middle
			next_square = (middle + 1) * (middle + 1)
			
			# found it ... cannot be equal to next square (ceil)
			if square <= x < next_square:
				return middle
			
			# binary search
			if square > x:
				end = middle - 1
			else:
				start = middle + 1
		
		# failed to find sqrt(x)
		return -1
			

s = Solution()
print s.mySqrt(2147395599)