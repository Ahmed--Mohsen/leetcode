"""

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""
class Solution:
	
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if len(prices) <= 1:
			return 0
			
		left = [0] * (len(prices)) # maximum profit gain in prices[0:left]
		right = [0] * (len(prices)) # maximum profit gain in prices[right:n]
		
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