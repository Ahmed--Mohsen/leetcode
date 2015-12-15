"""

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""

class Solution:
    # @param A, a list of integer
    # @return a List[int]
    def singleNumber(self, A):
			n = len(A)
			
			# pass 1
			# get the xor of the 2 numbers in question
			xor = 0
			for i in range(n):
				xor ^= A[i]
			
			# get the last set bit (rightmost)
			diff_bit = xor & -xor

			# pass 2
			# now different bit holds the position of the bit
			# that is different in the 2 numbers
			numbers = [0, 0]
			for i in range(n):
				
				# group 1 that has the diff bit not set
				if A[i] & diff_bit == 0:
					numbers[0] ^= A[i]
				
				# group 2 that has the diff bit set
				else:
					numbers[1] ^= A[i]			
			
			return numbers


s = Solution()
print s.singleNumber([1,1,2,2,3,5])