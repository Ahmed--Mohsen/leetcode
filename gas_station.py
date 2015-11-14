"""

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

"""

class Solution:
	
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		total = len(gas)
		tank = 0
		start = 0
		
		for i in range(total * 2):
			current = (i) % total
			next = (i+1) % total
			
			new_tank = tank - cost[current] + gas[current]
			if new_tank >= 0:
				tank = new_tank
				
				# make a succes round
				if next == start: 
					return start
			
			# reset and start from next position
			else:
				tank = 0
				start = next
		
		# failed to make a full round
		return -1