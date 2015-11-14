"""

Count the number of prime numbers less than a non-negative number, n.

"""

import math

class Solution:
	
	# @param {integer} n
	# @return {integer}
	def countPrimes(self, n):
		is_prime = [True] * n
		
		for i in range(2, int(math.sqrt(n)) + 1):
			
			# check if i is prime
			if is_prime[i]:

				# mark all i multiples as non primes
				j = i * i # no need to start from i (marked before)
				while j < n:
					is_prime[j] = False
					j += i
			
		# count the true is_prime entries
		prime_count = 0
		for i in range(2, n):
			if is_prime[i]:
				prime_count += 1
		return prime_count
				

s = Solution()
print s.countPrimes(20)