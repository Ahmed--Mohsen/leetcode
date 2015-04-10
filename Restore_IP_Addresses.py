class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		self.ips = []
		self.restoreIpAddressesHelper(s, 0, [])
		return self.ips
	
	def restoreIpAddressesHelper(self, s, start, ip):
		if start >= len(s) and len(ip) == 4:
			self.ips.append(".".join(ip))
		
		for size in range(1, min(3 + 1, len(s) - start + 1)):
			ip_part = s[start:start+size]
			if self.valid_ip(ip_part) and len(ip) < 4 :
				ip.append(ip_part)
				self.restoreIpAddressesHelper(s, start+size, ip)
				ip.pop()
				
	def valid_ip(self, ip_part):
		ip_part_val = int(ip_part)
		if ip_part_val > 255:
			return False
		if len(ip_part) > 1 and ip_part[0] == "0":
			return False
		return True
		
		
s = Solution()
print s.restoreIpAddresses("25525511135")