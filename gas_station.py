class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		total = len(gas)
		gas_amount = 0
		start = 0;
		for i in range(total * 2):
			current = (i) % total
			next = (i+1) % total
			if gas_amount - cost[current] + gas[current] >= 0:
				gas_amount = gas_amount - cost[current] + gas[current]
				if next == start: #make a succes round
					return start
			else:
				gas_amount = 0
				start = next
		return -1