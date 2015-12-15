"""

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""

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