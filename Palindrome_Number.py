"""

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

"""

class Solution:
	
	# @return an integer
	def isPalindrome(self, x):
		# base case
		if x < 0: return False
			
		normal = x
		reverse = 0
		
		while x > 0:
			reverse = (reverse * 10) + (x % 10)
			x = x  / 10
			
		return normal == reverse

s = Solution()
print s.isPalindrome(1321)