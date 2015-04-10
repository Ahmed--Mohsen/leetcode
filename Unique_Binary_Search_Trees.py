class Solution:
	# @return an integer
	def numTrees(self, n):
		trees = [0] * (n+1)
		
		#base cases
		trees[0] = 1 #for calculation to be correct (NONE Root)
		trees[1] = 1 #if only one number there is only one way
		
		#calculate unique BST when there is i numbers
		for i in range(2, n+1):
			#calculate uniques BST when j is root
			for j in range(1, i+1):
				#number of ways = (adding j-1 to left subtree) * (add i-j to right subtree)
				trees[i] += trees[j-1] * trees[i-j]
				
		return trees[n]
		

s = Solution()
print s.numTrees(3)