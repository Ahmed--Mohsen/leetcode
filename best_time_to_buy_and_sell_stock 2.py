class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		total = 0
		for i in range(len(prices) - 1):
			today = prices[i]
			tomorrow = prices[i+1]
			if tomorrow > today:
				total += (tomorrow - today)
		return total