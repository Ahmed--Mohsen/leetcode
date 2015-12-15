"""

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""

class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		ips = []
		self.restoreIpAddressesHelper(s, 0, [], ips)
		return ips
	
	def restoreIpAddressesHelper(self, s, start, ip, result):
		# base case
		if start >= len(s) and len(ip) == 4:
			result.append(".".join(ip))
		
		# max size that can be reached from start
		max_size = min(3, len(s) - start)
		
		for size in range(1, max_size + 1):
			ip_part = s[start : start+size]
			
			# valid ip chunck
			if self.valid_ip(ip_part) and len(ip) < 4 :
				ip.append(ip_part)
				self.restoreIpAddressesHelper(s, start+size, ip, result) # recurse
				ip.pop() # backtrack
				
				
	def valid_ip(self, ip_part):
		ip_part_val = int(ip_part)
		if ip_part_val > 255:
			return False
		if len(ip_part) > 1 and ip_part[0] == "0":
			return False
		return True
		
		
s = Solution()
print s.restoreIpAddresses("25525511135")