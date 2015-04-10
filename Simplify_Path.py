class Solution:
	# @param path, a string
	# @return a string
	def simplifyPath(self, path):
		paths = path.split("/")
		result = []
		
		for i in range(len(paths)):
			if paths[i] == "" or paths[i] == ".":
				continue			
				
			elif paths[i] == "..":
				if len(result) > 0:
					result.pop()
					
			else:
				result.append(paths[i])
				
		return "/" + "/".join(result)

s = Solution()
print s.simplifyPath("/..")