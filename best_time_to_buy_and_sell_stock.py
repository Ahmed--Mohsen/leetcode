class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if len(prices) == 0:
			return 0
		profit = 0
		buy = prices[0]
		for price in prices:
			buy = min(buy, price)
			profit = max(profit, price - buy)
		return profit