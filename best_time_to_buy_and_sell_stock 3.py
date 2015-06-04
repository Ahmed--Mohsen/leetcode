class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if len(prices) <= 1:
			return 0
			
		left = [0] * (len(prices)) #maximum profit gain in prices[0:left]
		right = [0] * (len(prices)) #maximum profit gain in prices[right:n]
		
		# move from left to right
		min_price = prices[0]
		for i in range(1, len(prices)):
			min_price = min(min_price, prices[i])
			left[i] = max(left[i-1], prices[i] - min_price)
		
		# move from right to left
		max_price = prices[-1]
		for i in range(len(prices)-2, -1, -1):
			max_price = max(max_price, prices[i])
			right[i] = max(right[i+1], max_price - prices[i])
		
		# get the best of sum of left and right
		best = 0
		for i in range(len(prices) - 1):
			best = max(best, left[i] + right[i])
		return best
		
s = Solution()
print s.maxProfit([1,2])