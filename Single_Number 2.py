"""

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		t1 = 0; t2 = 0; t3 = 0

		for a in A:
			t2 = t2 | (t1 & a)
			t1 = t1 ^ a
			t3 = ~(t1 & t2)
			t1 = t1 & t3
			t2 = t2 & t3

		return t1