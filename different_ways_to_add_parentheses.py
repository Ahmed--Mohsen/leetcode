"""

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

"""

class Solution(object):
	
	"""
	:type input: str
	:rtype: List[int]
	"""
	def diffWaysToCompute(self, input):
		# base case
		if len(input) == 0:
			return []
		
		# for easier calculations
		operations = {
			'+' : lambda x, y: x + y,
			'-' : lambda x, y: x - y,
			'*' : lambda x, y: x * y
		}
		
		# dynamic programming memo
		dp = {}
		
		return self.diffWaysToComputeHelper(input, operations, dp)
		
	
	def diffWaysToComputeHelper(self, inp, ops, dp):
		result = []
		
		size = len(inp)
		for i in range(size):
			current = inp[i]
			
			# needs to split the input
			if current in "+-*":
				left_inp = inp[:i]
				right_inp = inp[i+1:]
				
				left = dp[left_inp] if left_inp in dp else self.diffWaysToComputeHelper(left_inp, ops, dp)
				right = dp[right_inp] if right_inp in dp else self.diffWaysToComputeHelper(right_inp, ops, dp)
				
				# calc all combinations
				for l in left:
					for r in right:
						result.append(ops[ current ](l, r))
			
		
		# empty result mean the input is a number
		if not result:
			result.append(int(inp))
		
		# save result in memo
		dp[inp] = result
		
		return result


s = Solution()
print s.diffWaysToCompute("2-1-1")
