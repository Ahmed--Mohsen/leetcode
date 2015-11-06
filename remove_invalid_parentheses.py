"""

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""

from collections import deque

class Solution(object):
	
	"""
	:type s: str
	:rtype: List[str]
	"""
	def removeInvalidParentheses(self, s):
		result = []
		
		# base case
		if s == None:
			return result
		
		# perfrom bfs as long as the current level
		# doesn't have a valid string (shortest path) i.e min 
		# num of removal (when result found step at the cuurent level)
		queue = deque([s])
		visited = set()
		found = False
		
		while queue:
			current = queue.popleft()
			
			# if current string is valid no need to continue search
			if self.isValid(current):
				result.append(current)
				found = True # stop other levels search
			
			# try removal of every ( or )
			elif not found:
				for i in range(len(current)):
					
					# only try to remove left or right paren
					if current[i] != '(' and current[i] != ')': continue
					
					# try the removal
					next = current[:i] + current[i+1:]
					if not next in visited:
						visited.add(next)
						queue.append(next)
				
		return result
		
	
	"""
	check if s is valid Parenthesesed string
	"""
	def isValid(self, s):
		count = 0
		
		for c in s:
			
			if c == "(":
				count += 1
				
			if c == ")":
				count -= 1
				
				# early stop
				if count < 0:
					return False
		
		return count == 0

	
s = Solution()
print s.removeInvalidParentheses("()())()")