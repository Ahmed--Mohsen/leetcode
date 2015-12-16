"""

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

"""
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