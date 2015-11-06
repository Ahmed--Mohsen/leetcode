"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

"""
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