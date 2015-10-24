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