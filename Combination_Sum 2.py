"""

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6]

"""

class Solution:
	
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		result = []
		candidates.sort()
		self.combinationSumHelper(candidates, 0, target, [], result)
		return result
	
	
	def combinationSumHelper(self, candidates, start, target, combination, result):
		# base case we reached the target
		if target == 0: 
			result.append(list(combination))
			return
		
		for i in range(start, len(candidates)):
			
			# skip duplicates
			if i > start and candidates[i] == candidates[i-1]: continue
			
			new_target = target - candidates[i]
			
			# can lead to new combination
			if new_target >= 0: 
				combination.append(candidates[i])
				self.combinationSumHelper(candidates, i+1, new_target, combination, result) # recurse
				combination.pop() # backtrack

			# no way to get to the target from this start as array is sorted
			else: 
				break
				
				
				
s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5], 8)