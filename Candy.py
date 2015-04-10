class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		r = len(ratings)
		candies = [1] * r
		
		#move from left to right
		for i in range(1, r):
			candies[i] = candies[i-1] + 1 if ratings[i] > ratings[i-1] else candies[i]
		
		#move from right to left
		total = candies[-1]
		for i in range(r-2, -1, -1):
			candies[i] = candies[i+1] + 1 if (ratings[i] > ratings[i+1] and candies[i+1] >= candies[i]) else candies[i]
			total += candies[i]
	
		return total


s = Solution()

print s.candy([1,5,3,1])