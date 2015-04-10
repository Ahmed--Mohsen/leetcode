class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum(self, candidates, target):
		result = []
		candidates.sort()
		self.candidates = candidates
		self.combinationSumHelper(0, target, [], result)
		return result
	
	
	def combinationSumHelper(self, start, target, combination, result):
		if target == 0: #base case we reached the target
			result.append(list(combination))
			return
		
		for i in range(start, len(self.candidates)):
			new_target = target - self.candidates[i]
			if new_target >= 0: #can lead to new combination
				combination.append(self.candidates[i])
				self.combinationSumHelper(i, new_target, combination, result) #recurse
				combination.pop() #backtrack
			else: #no way to get to the target from this start
				break
				
				
s = Solution()
print s.combinationSum([2,3,6,7], 7)