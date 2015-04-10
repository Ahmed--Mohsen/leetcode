class Solution:
	# @param version1, a string
	# @param version2, a string
	# @return an integer
	def compareVersion(self, version1, version2):
		if version1 == version2:
			return 0
		
		v1 = [int(x) for x in version1.split(".")]
		v2 = [int(x) for x in version2.split(".")]
		
		min_v = min(len(v1), len(v2))
		
		for i in range(min_v):
			if v1[i] > v2[i]:
				return 1
			if v1[i] < v2[i]:
				return -1
				
		if len(v1) == len(v2):
			return 0
		
		if len(v1) > len(v2):
			for i in range(min_v, len(v1)):
				if v1[i] > 0:
					return 1
		else: #len(v1) < len(v2)
			for i in range(min_v, len(v2)):
				if v2[i] > 0:
					return -1
			
		return 0