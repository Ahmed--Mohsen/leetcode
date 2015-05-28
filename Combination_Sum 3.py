class Solution:
	# @param {integer} k
	# @param {integer} n
	# @return {integer[][]}
	def combinationSum3(self, k, target):
		result = []
		self.candidates = [i for i in range(1,10)]
		self.target_steps = k
		self.combinationSumHelper(0, target, 0, [], result)
		return result
	
	
	def combinationSumHelper(self, start, target, steps ,combination, result):
		if target == 0 and steps == self.target_steps: #base case we reached the target
			result.append(list(combination))
			return
		
		for i in range(start, len(self.candidates)):
			new_target = target - self.candidates[i]
			if new_target >= 0 and steps < self.target_steps: #can lead to new combination
				combination.append(self.candidates[i])
				self.combinationSumHelper(i+1, new_target, steps + 1,combination, result) #recurse
				combination.pop() #backtrack
			else: #no way to get to the target from this start
				break
				
				
s = Solution()
print s.combinationSum3(3, 9)