"""

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

"""

ASCII = 256
class Solution:
	
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		n = len(s)
		
		# base case
		if n < 2: return n
		
		# maps last occurance of an ASCII char to its position
		# using -1 as intial value to mimic hashmap when doesn't
		# contain a certain key
		memo = [-1] * ASCII
		
		
		# starting position of active substring 
		start = 0
		
		# max length of found substring so far
		max_len = 0
		
		# loop over each ending for active string
		for i in range(n):
			
			# active substring would be broken
			if memo[ord(s[i])] >= start:
				# skip to next place where there is no duplicates with i
				start = memo[ord(s[i])] + 1 
			
			# keep track of latest position for s[i]
			memo[ord(s[i])] = i
			
			# length of current active subtring = i - start + 1
			max_len = max(max_len, i - start + 1);

		return max_len


s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")
		