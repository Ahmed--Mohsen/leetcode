class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		result = []
		candidates.sort()
		self.candidates = candidates
		self.combinationSumHelper(0, target, [], result)
		return result
	
	
	def combinationSumHelper(self, start, target, combination, result):
		if target == 0: #base case we reached the target
			result.append(list(combination))
			return
		
		if start >= len(self.candidates):
			return
		
		new_target = target - self.candidates[start]
		if new_target >= 0: #can lead to new combination
			combination.append(self.candidates[start])
			self.combinationSumHelper(start+1, new_target, combination, result) #recurse
			combination.pop() #backtrack
			
			#skip duplicates ... by finding the next start to search from after finshing
			#current recurse
			i = start + 1
			while i < len(self.candidates) and self.candidates[i] == self.candidates[i-1]: 
				i += 1
			self.combinationSumHelper(i, target, combination, result) #recurse to next non duplicate
			
				
				
s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5], 8)